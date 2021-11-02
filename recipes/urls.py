from django.urls import path
from .views import show_recipe, create_recipe, delete_recipe, update_recipe


urlpatterns = [
    path('<int:recipe_id>/', show_recipe, name='show_recipe'),
    path('create/', create_recipe, name='create_recipe'),
    path('delete_recipe/<int:recipe_id>/', delete_recipe, name='delete_recipe'),
    path('update_recipe/<int:recipe_id>/', update_recipe, name='update_recipe')
]
