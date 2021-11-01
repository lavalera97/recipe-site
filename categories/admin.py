from django.contrib import admin
from . import models
from recipes.models import Recipe


class RecipeInline(admin.TabularInline):
    model = Recipe
    extra = 0


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug', 'updated_at', 'created_at')
    ordering = ('category_name',)
    readonly_fields = ('updated_at', 'created_at')
    # prepopulated_fields = {'slug': ('category_name',)}
    inlines = [RecipeInline]
