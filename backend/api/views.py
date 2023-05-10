from rest_framework import mixins, permissions
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.decorators import login_required

from users.models import FoodgramUser, Follow

from .serializers import UserSerializer
from rest_framework.response import Response


class UserViewSet(ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = FoodgramUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    @login_required
    def profile_follow(request, username):
        user = request.user
        author = FoodgramUser.objects.get(username=username)
        serializer = SubscribeSerializer(author, data=request.data, context={"request": request})
        follow = Follow.objects.filter(user=user, author=author)
        if user != author and not follow.exists():
            Follow.objects.create(
                user=user,
                author=author,
            )
        return Response(serializer.data)