from categories.models import Category


def show_categories(request):
    """Context processor, который позволяет получить информацию о категориях на любой странице"""
    categories = Category.objects.all().order_by('-updated_at')
    return dict(categories=categories)