from djoser.views import TokenDestroyView

from rest_framework import mixins, permissions
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from rest_framework_simplejwt.authentication import JWTAuthentication

from users.models import FoodgramUser

from .serializers import UserSerializer


class UserViewSet(ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = FoodgramUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class TokenDestroyAPIView(TokenDestroyView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.auth_token.delete()

        return Response(status=204)
