from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import UniqueConstraint

User = get_user_model()


class Tag(models.Model):

    name = models.CharField(
        max_length=200,
        verbose_name='Название Тэга',
        blank=False
    )
    color = models.CharField(
        max_length=7,
        unique=True,
        verbose_name='Цвет',
        validators=[RegexValidator(
            regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
            message='Введите значение в HEX-формате'
        )]
    )

    slug = models.SlugField(
        max_length=200,
        verbose_name='slug',
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


class Ingredients(models.Model):

    name = models.CharField(
        max_length=200,
        verbose_name='Ингредиент',
        blank=False
    )
    measurement_unit = models.CharField(
        max_length=200,
        verbose_name='Единицы измерения',
        blank=False
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Recipe(models.Model):
    name = models.CharField('Название', max_length=200)
    author = models.ForeignKey(
        User,
        related_name='recipes',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор',
    )
    text = models.TextField('Описание')
    image = models.ImageField(
        'Изображение',
        upload_to='recipes/images/'
    )
    cooking_time = models.PositiveSmallIntegerField()
    ingredients = models.ManyToManyField(
        Ingredients,
        through='IngredientInRecipe',
        related_name='recipes',
        verbose_name='Ингредиенты'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Теги'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientInRecipe(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredient_list',
        verbose_name='Рецепт',
    )
    ingredient = models.ForeignKey(
        Ingredients,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество',
    )

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиенты в рецептах'

    def __str__(self):
        return (
            f'{self.ingredient.name} ({self.ingredient.measurement_unit})'
            f' - {self.amount} '
        )


class Favourites(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Рецепт',
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        constraints = [UniqueConstraint(
            fields=['user', 'recipe'],
            name='unique_favourite'
        )]

    def __str__(self):
        return f'{self.user} добавил "{self.recipe}" в Избранное'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Рецепт',
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Список покупок'
