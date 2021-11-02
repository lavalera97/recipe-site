from django.contrib import admin
from .models import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Показывает ингредиенты в админ панеле"""
    list_display = ('ingredient_name', 'slug')
    ordering = ('ingredient_name',)
    search_fields = ('ingredient_name', 'slug')
    prepopulated_fields = {'slug': ('ingredient_name',)}

