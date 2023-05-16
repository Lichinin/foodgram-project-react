from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet

from api.filters import IngredientFilter, RecipeFilter
from api.permissions import IsAdmin, IsSuperUserIsAdminIsModeratorIsAuthor

from .models import Favourites, Ingredients, Recipe, ShoppingCart, Tag
from .serializers import (IngredientInRecipe, IngredientsSerializer,
                          RecipeReadSerializer, RecipeSerializerShort,
                          RecipeWriteSerializer, TagSerializer)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    pagination_class = None
    filter_backends = (DjangoFilterBackend,)
    filterset_class = IngredientFilter
    search_fields = ("name",)


class RecipesViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    permission_classes = (IsSuperUserIsAdminIsModeratorIsAuthor | IsAdmin,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipeFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return RecipeReadSerializer
        return RecipeWriteSerializer

    @action(
        detail=True,
        methods=['post', 'delete'],
        permission_classes=[IsSuperUserIsAdminIsModeratorIsAuthor]
    )
    def favorite(self, request, pk):
        if request.method == 'POST':
            return self.add_to(Favourites, request.user, pk)
        else:
            return self.delete_from(Favourites, request.user, pk)

    @action(
        detail=True,
        methods=['post', 'delete'],
        permission_classes=[IsAuthenticated]
    )
    def shopping_cart(self, request, pk):
        if request.method == 'POST':
            return self.add_to(ShoppingCart, request.user, pk)
        else:
            return self.delete_from(ShoppingCart, request.user, pk)

    def add_to(self, model, user, pk):
        if model.objects.filter(user=user, recipe__id=pk).exists():
            return Response({'errors': 'Такой рецепт уже есть'},
                            status=status.HTTP_400_BAD_REQUEST)
        recipe = get_object_or_404(Recipe, id=pk)
        model.objects.create(user=user, recipe=recipe)
        serializer = RecipeSerializerShort(recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete_from(self, model, user, pk):
        obj = model.objects.filter(user=user, recipe__id=pk)
        if obj.exists():
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'errors': 'Рецепт удален'},
                        status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=False,
        permission_classes=[IsAuthenticated]
    )
    def download_shopping_cart(self, request):
        user = request.user
        if not user.shopping_cart.exists():
            return Response(status=HTTP_400_BAD_REQUEST)

        ingredients = IngredientInRecipe.objects.filter(
            recipe__shopping_cart__user=request.user
        ).values(
            'ingredient__name',
            'ingredient__measurement_unit'
        ).annotate(amount=Sum('amount'))

        pdfmetrics.registerFont(
            TTFont('Times New Roman', 'Times.ttf', 'UTF-8'),
        )
        pdfmetrics.registerFont(
            TTFont('Times New Roman Bold', 'timesbd.ttf', 'UTF-8')
        )
        filename = f'{user.username}_shopping_list.txt'
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={filename}'
        p = canvas.Canvas(response)
        p.setFont("Times New Roman Bold", 18)
        p.drawString(
            10, 800, f'Список покупок пользователя {user.get_full_name()}'
        )
        p.setFont("Times New Roman", 12)
        stroke = 700
        for ingredient in ingredients:
            p.drawString(
                20,
                stroke, f'* {ingredient["ingredient__name"]} - {ingredient["amount"]} {ingredient["ingredient__measurement_unit"]}'
            )
            stroke -= 25

        p.showPage()
        p.save()

        return response
