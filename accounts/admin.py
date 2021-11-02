from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from recipes.models import Recipe


class RecipeInline(admin.TabularInline):
    """Показывает рецепты, которые сделал пользователь"""
    model = Recipe
    extra = 0


@admin.register(Account)
class AccountAdmin(UserAdmin):
    """Создаёт модель для показа аккаунта пользователя в админ панеле"""
    list_display = ('email', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'username')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    list_editable = ('is_active',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    inlines = [RecipeInline]