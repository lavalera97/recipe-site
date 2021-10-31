from django.urls import path
from .views import register, logout


urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', logout, name='logout')

]