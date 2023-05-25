from django.contrib import admin
from django.contrib.admin import display

from .models import (
    Favourites, IngredientInRecipe, Ingredients, Recipe, ShoppingCart, Tag
)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name_icontains',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'in_favoutites_count')
    list_filter = ('author', 'name', 'tags')

    @display(description='Добавлений в избранное')
    def in_favoutites_count(self, obj):
        return obj.favorites.count()


@admin.register(IngredientInRecipe)
class IngredientInRecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')


@admin.register(Favourites)
class FavouritesAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('user',)
