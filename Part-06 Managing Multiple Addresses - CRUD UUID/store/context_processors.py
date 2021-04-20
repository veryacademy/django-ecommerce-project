from .models import Category


def categories(request):
    return {"categories": Category.objects.filter(level=0)}
