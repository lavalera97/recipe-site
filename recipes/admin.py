from django.contrib import admin
from .models import Recipe
from ingredients.models import Ingredient


@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    list_display = ('recipe_name', 'category', 'active')
    ordering = ('created_at',)
    list_filter = ('category',)
    search_fields = ('recipe_name',)
    list_editable = ('active',)


class RecipeIngredientInline(admin.TabularInline):
    model = Ingredient
    readonly_fields =('ingredient_name',)