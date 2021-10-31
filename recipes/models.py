from django.db import models
from django.shortcuts import reverse
from categories.models import Category
from ingredients.models import Ingredient
from ckeditor.fields import RichTextField


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=40, verbose_name='Название рецепта')
    description = models.TextField(max_length=600, blank=True, verbose_name='Краткое описание рецепта')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория рецепта')
    image = models.ImageField(upload_to='images/recipes', blank=True, verbose_name='Картинка продукта')
    prep_time = models.CharField(max_length=20, blank=True, verbose_name='Заготовка продукта')
    cook_time = models.CharField(max_length=20, blank=True, verbose_name='Время в печи')
    all_time = models.CharField(max_length=20, verbose_name='Общее время для приготовления')
    ingredients = models.ManyToManyField(Ingredient, verbose_name='Ингредиенты продукта')
    recipe_to_cook = RichTextField(max_length=2000, verbose_name='Рецепт для готовки')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField('Время создания записи', auto_now_add=True)
    updated_at = models.DateTimeField('Время обновления записи', auto_now=True)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def get_url(self):
        return reverse('show_recipe', kwargs={'recipe_id': self.id})

    def __str__(self):
        return self.recipe_name
