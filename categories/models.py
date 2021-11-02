from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    """Модель для создания категории"""
    category_name = models.CharField(max_length=30, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=40, unique=True, verbose_name='Ссылка на категорию')
    description = models.TextField(max_length=200, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images/categories', blank=True, verbose_name='Картинка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания записи')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления записи')

    class Meta:
        """Изменяет имена в админ панеле"""
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_category_recipes(self):
        """Показывает рецепты выбранной категории"""
        return reverse('home', kwargs={'category_slug': self.slug})

    def __str__(self):
        """При обращении str к моделе показывает название категории"""
        return self.category_name
