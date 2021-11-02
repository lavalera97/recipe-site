from django.db import models
from django.shortcuts import reverse
from categories.models import Category
from ingredients.models import Ingredient
from accounts.models import Account
from ckeditor.fields import RichTextField


class Recipe(models.Model):
    """Модель для создания рецептов"""
    COMPLEXITY_CHOICES = [
        ('Лёгкая', 'Легкая'),
        ('Средняя', 'Средняя'),
        ('Тяжёлая', 'Тяжелая')
    ]

    recipe_name = models.CharField(max_length=60, verbose_name='Название рецепта')
    description = models.TextField(max_length=600, blank=True, verbose_name='Краткое описание рецепта')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория рецепта')
    image = models.ImageField(upload_to='images/recipes', blank=True, verbose_name='Картинка продукта')
    author = models.ForeignKey(Account, on_delete=models.SET_NULL, verbose_name='Автор рецепта', blank=True, null=True)
    all_time = models.CharField(max_length=20, verbose_name='Общее время для приготовления')
    complexity = models.CharField(max_length=20, verbose_name='Сложность готовки', blank=True, choices=COMPLEXITY_CHOICES)
    ingredients = models.ManyToManyField(Ingredient, verbose_name='Ингредиенты продукта', related_name='ingredients')
    recipe_to_cook = RichTextField(max_length=2000, verbose_name='Рецепт для готовки')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField('Время создания записи', auto_now_add=True)
    updated_at = models.DateTimeField('Время обновления записи', auto_now=True)

    class Meta:
        """Изменяет имена в админ панеле"""
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def get_url(self):
        """Возвращает url к рецепту"""
        return reverse('show_recipe', kwargs={'recipe_id': self.id})

    def __str__(self):
        """При обращении str к моделе показывает название категории"""
        return self.recipe_name
