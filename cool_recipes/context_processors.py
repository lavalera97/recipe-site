from categories.models import Category


def show_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)