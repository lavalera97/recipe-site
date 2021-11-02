from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Recipe
from ingredients.models import Ingredient
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm


def return_ingredients(request):
    ingredients = []
    recipe_ingredients = []
    for i in range(0, 20):
        ingredient = request.POST.get(f'ingredient_name[{i}]')
        if ingredient and (ingredient not in ingredients):
            ingredients.append(ingredient)
    for i in ingredients:
        if not Ingredient.objects.filter(ingredient_name__iexact=i).exists():
            ingred = Ingredient.objects.create(ingredient_name=i)
            ingred.save()
        recipe_ingredients.append(Ingredient.objects.get(ingredient_name__iexact=i))
    return recipe_ingredients


def show_recipe(request, recipe_id):
    """Функция показывает выбранный рецепт"""
    recipe = get_object_or_404(Recipe, id=recipe_id, active=True)
    ingredients = recipe.ingredients.all().order_by('ingredient_name')
    context = {
        'recipe': recipe,
        'ingredients': ingredients
    }

    return render(request, 'recipe_info.html', context)


@login_required(login_url='login')
def create_recipe(request):
    """Функция позволяет создавать рецепт"""
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe_name = recipe_form.cleaned_data['recipe_name']
            description = recipe_form.cleaned_data.get('description')
            category = recipe_form.cleaned_data['category']
            image = recipe_form.cleaned_data.get('image')
            author = request.user
            all_time = recipe_form.cleaned_data['all_time']
            complexity = recipe_form.cleaned_data.get('complexity')
            recipe_to_cook = recipe_form.cleaned_data['recipe_to_cook']
            recipe_ingredients = return_ingredients(request)
            recipe = Recipe.objects.create(recipe_name=recipe_name, description=description, category=category, image=image,
                                           author=author, all_time=all_time, complexity=complexity, recipe_to_cook=recipe_to_cook)
            recipe.save()
            recipe.ingredients.set(recipe_ingredients)
            return redirect('home')
    else:
        recipe_form = RecipeForm()
    context = {
        'recipe_form': recipe_form

    }
    return render(request, 'create_update_recipe.html', context)


@login_required(login_url='login')
def update_recipe(request, recipe_id):
    """Функция позволяет обновить рецепт"""
    recipe = Recipe.objects.get(pk=recipe_id)
    recipe_exist_name = recipe.recipe_name
    if recipe.author != request.user:
        return redirect('home')

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if recipe_form.is_valid():
            recipe.author = request.user
            recipe_form.save()
            recipe_ingredients = return_ingredients(request)
            recipe.ingredients.set(recipe_ingredients)
            return HttpResponseRedirect(reverse('show_recipe', kwargs={'recipe_id': recipe.id}))
    else:
        recipe_form = RecipeForm(instance=recipe)
    context = {
        'recipe': recipe,
        'recipe_form': recipe_form,
        'recipe_exist_name': recipe_exist_name
    }
    return render(request, 'create_update_recipe.html', context)


@login_required(login_url='login')
def delete_recipe(request, recipe_id):
    """Функция удаляет рецепт"""
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
        if recipe.author == request.user:
            recipe.delete()
            return HttpResponseRedirect(reverse('show_profile', kwargs={'account_name': recipe.author.username}))
        else:
            return redirect('home')
    except Recipe.DoesNotExist:
        return redirect('home')

