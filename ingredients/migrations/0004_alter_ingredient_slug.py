# Generated by Django 3.2.8 on 2021-11-02 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0003_delete_recipeingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='slug',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
