# Generated by Django 3.2.8 on 2021-11-01 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20211101_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='cook_time',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='prep_time',
        ),
    ]
