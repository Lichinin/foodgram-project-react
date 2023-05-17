from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import UniqueConstraint


class UserRoles(Enum):
    user = 'user'
    admin = 'admin'


USER_ROLES_CHOICES = [(role.name, role.value) for role in UserRoles]


class FoodgramUser(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(
        max_length=254,
        verbose_name='email',
        unique=True,
        blank=False
    )
    username = models.CharField(
        max_length=150,
        verbose_name='Логин',
        unique=True,
        blank=False,
        validators=[RegexValidator(
            regex=r'^[\w.@+-]+$',
            message='Имя пользователя содержит недопустимый символ'
        )]
    )
    role = models.CharField(
        max_length=20,
        verbose_name='роль',
        choices=USER_ROLES_CHOICES,
        default=UserRoles.user.name
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == UserRoles.admin.name

    @property
    def is_user(self):
        return self.role == UserRoles.user.name

    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']


class Follow(models.Model):
    user = models.ForeignKey(
        FoodgramUser,
        on_delete=models.CASCADE,
        verbose_name='Подписчик',
        related_name='user',
    )
    author = models.ForeignKey(
        FoodgramUser,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='author',
    )

    class Meta:
        ordering = ['-id']
        constraints = [
            UniqueConstraint(fields=['user', 'author'],
                             name='unique_subscription')
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
