from django.db import models


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50, unique=True, verbose_name='Название ингредиента')
    slug = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField('Время создания записи', auto_now_add=True)
    updated_at = models.DateTimeField('Время обновления записи', auto_now=True)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.ingredient_name



