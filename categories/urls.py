from django.urls import path
from cool_recipes.views import home

urlpatterns = [
    path('<slug:category_slug>/', home, name='home')

]