from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from accounts.models import Account
from recipes.models import Recipe
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required


def register(request):
    """Функция для регистрации пользователя"""
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = Account.objects.create_user(username=username,
                                               email=email,
                                               password=password)
            user.is_active = True
            user.save()
            messages.success(request, "Вы успешно зарегестрировались")
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login(request):
    """Функция для входа пользователя"""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Неправильный email или пароль')
    return render(request, 'login.html')


@login_required(login_url='login')
def logout(request):
    """Функция для выхода пользователя"""
    auth.logout(request)
    url = request.META.get('HTTP_REFERER')
    return redirect(url)


def show_profile(request, account_name):
    """Функция для показа профиля"""
    account = get_object_or_404(Account, username=account_name)
    recipes = Recipe.objects.filter(author=account)
    context = {
        'account': account,
        'recipes': recipes,
    }
    return render(request, 'profile.html', context)
