from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """Форма для создания рецептов"""
    class Meta:
        model = Recipe
        exclude = ['active', 'created_at', 'updated_at', 'ingredients']

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['recipe_name'].widget.attrs['placeholder'] = 'Название рецепта'
        self.fields['description'].widget.attrs['placeholder'] = 'Описание рецепта'
        self.fields['all_time'].widget.attrs['placeholder'] = 'Общее время приготовления'
        self.fields['complexity'].widget.attrs['placeholder'] = 'Сложность блюда'
        self.fields['recipe_to_cook'].widget.attrs['placeholder'] = 'Рецепт приготовления блюда'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
