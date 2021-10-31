from django.shortcuts import render
from categories.models import Category
from django.shortcuts import get_object_or_404
from recipes.models import Recipe


def home(request, category_slug=None):
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        recipes = Recipe.objects.filter(category=category)
        context = {
            'recipes': recipes,
            'category': category
        }
    else:
        recipes = Recipe.objects.all()
        context = {
            'recipes': recipes
        }
    return render(request, 'home_page.html', context)
