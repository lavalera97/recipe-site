from django.shortcuts import render
from categories.models import Category


def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    print(categories)
    return render(request, 'home_page.html', context)
