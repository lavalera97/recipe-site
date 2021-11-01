from django.shortcuts import render
from categories.models import Category
from django.shortcuts import get_object_or_404
from recipes.models import Recipe
from django.db.models import Q


def search(ingredients, recipe_search_name):
    recipes = []
    if ingredients:
        if recipe_search_name != '':
            all_recipes = Recipe.objects.filter(Q(recipe_name__icontains=recipe_search_name)
                                                | Q(category__category_name__icontains=recipe_search_name))
        else:
            all_recipes = Recipe.objects.all()
        for recipe in all_recipes:
            right_recipe = True
            recipe_ingredient_names = [ingred.ingredient_name.lower() for ingred in recipe.ingredients.all()]
            for i in ingredients:
                if not any(i in elem for elem in recipe_ingredient_names):
                    right_recipe = False
            if right_recipe:
                recipes.append(recipe)
    else:
        recipes = Recipe.objects.filter(Q(recipe_name__icontains=recipe_search_name)
                                        | Q(category__category_name__icontains=recipe_search_name))
    return recipes


def home(request, category_slug=None):
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        recipes = Recipe.objects.filter(category=category).order_by('-updated_at')
        context = {
            'recipes': recipes,
            'category': category
        }
    else:
        recipes = Recipe.objects.all().order_by('-updated_at')
        context = {
            'recipes': recipes
        }
    return render(request, 'home_page.html', context)


def search_recipe(request):
    ingredients = []
    for i in range(0, 20):
        ingredient = request.GET.get(f'ingredient_name[{i}]')
        if ingredient and (ingredient not in ingredients):
            ingredients.append(ingredient.lower())

    recipe_search_name = request.GET.get('recipe_name')
    if not recipe_search_name:
        recipe_search_name = ''

    recipes = search(ingredients, recipe_search_name)

    context = {
        'recipes': recipes,
        'recipe_search_name': recipe_search_name,
        'ingredients': ingredients
    }
    return render(request, 'home_page.html', context)
