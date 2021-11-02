from django.urls import path
from .views import register, logout, login, show_profile


urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('profile/<str:account_name>/', show_profile, name='show_profile')

]