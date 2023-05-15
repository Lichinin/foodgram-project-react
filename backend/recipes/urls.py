from .views import IngredientViewSet, RecipesViewSet, TagViewSet

from django.urls import include, path

from rest_framework import routers

app_name = "recipes"

router = routers.DefaultRouter()
router.register('tags', TagViewSet)
router.register('ingredients', IngredientViewSet)
router.register('recipes', RecipesViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
