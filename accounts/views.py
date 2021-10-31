from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def register(request):
    form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def logout(request):
    auth.logout(request)
    url = request.META.get('HTTP_REFERER')
    return redirect(url)
