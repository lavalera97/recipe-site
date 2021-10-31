from django.urls import path
from .views import show_recipe


urlpatterns = [
    path('<int:recipe_id>/', show_recipe, name='show_recipe')

]
