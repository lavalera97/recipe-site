from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug')
    ordering = ('category_name',)
    # prepopulated_fields = {'slug': ('category_name',)}
