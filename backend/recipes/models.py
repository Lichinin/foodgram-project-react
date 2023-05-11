from django.core.validators import RegexValidator
from django.db import models


class Tag(models.Model):

    name = models.CharField(
        max_length=200,
        verbose_name='Название Тэга',
        blank=False
    )
    color = models.CharField(
        max_length=7,
        verbose_name='Цвет',
    )
    slug = models.SlugField(
        max_length=200,
        verbose_name='Цвет',
        validators=[RegexValidator(
            regex=r'^[-a-zA-Z0-9_]+$',
            message='Slug содержит недопустимый символ'
        )]
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name
