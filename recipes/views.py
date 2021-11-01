from django.shortcuts import render, get_object_or_404
from .models import Recipe
from categories.models import Category
from django.http import Http404


def show_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, active=True)
    ingredients = recipe.ingredients.all().order_by('ingredient_name')
    context = {
        'recipe': recipe,
        'ingredients': ingredients
    }

    return render(request, 'recipe_info.html', context)
