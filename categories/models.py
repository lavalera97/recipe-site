from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=40, unique=True, verbose_name='Ссылка на категорию')
    description = models.TextField(max_length=200, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images/categories', blank=True, verbose_name='Картинка')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name
