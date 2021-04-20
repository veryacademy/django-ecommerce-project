from .models import Category


def categories(request):
    return {
        'categories': Category.objects.all()
    }
