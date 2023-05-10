from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRoles(Enum):
    """Перечисление пользовательских ролей."""

    user = 'user'
    admin = 'admin'

    @classmethod
    def choices(cls):
        return tuple((attribute.name, attribute.value) for attribute in cls)


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
        blank=False
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя пользователя',
        blank=False
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия пользователя',
        blank=False
    )
    role = models.CharField(
        max_length=20,
        verbose_name='роль',
        choices=UserRoles.choices(),
        default=UserRoles.user.name
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=150,
        help_text='Введите пароль',
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

    REQUIRED_FIELDS = ["first_name", "last_name", ]
