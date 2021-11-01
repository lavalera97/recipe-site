from categories.models import Category


def show_categories(request):
    categories = Category.objects.all().order_by('-updated_at')
    return dict(categories=categories)