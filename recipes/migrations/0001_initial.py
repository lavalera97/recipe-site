# Generated by Django 3.2.8 on 2021-10-30 18:01

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_auto_20211030_0019'),
        ('ingredients', '0003_delete_recipeingredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=40, unique=True, verbose_name='Название рецепта')),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=400, verbose_name='Краткое описание рецепта')),
                ('image', models.ImageField(blank=True, upload_to='images/recipes', verbose_name='Картинка продукта')),
                ('prep_time', models.CharField(blank=True, max_length=20, verbose_name='Заготовка продукта')),
                ('cook_time', models.CharField(blank=True, max_length=20, verbose_name='Время в печи')),
                ('all_time', models.CharField(blank=True, max_length=20, verbose_name='Общее время для приготовления')),
                ('recipe_to_cook', ckeditor.fields.RichTextField(max_length=600, verbose_name='Рецепт для готовки')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания записи')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления записи')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categories.category', verbose_name='Категория рецепта')),
                ('ingredients', models.ManyToManyField(to='ingredients.Ingredient', verbose_name='Ингредиенты продукта')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
    ]
