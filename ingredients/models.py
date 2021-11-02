from django.db import models


class Ingredient(models.Model):
    """Модель для создания ингредиентов"""
    ingredient_name = models.CharField(max_length=50, unique=True, verbose_name='Название ингредиента')
    slug = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField('Время создания записи', auto_now_add=True)
    updated_at = models.DateTimeField('Время обновления записи', auto_now=True)

    class Meta:
        """Имена показываемые для модели ингредиента в админ панеле"""
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        """При обращении str к моделе показывает название категории"""
        return self.ingredient_name



