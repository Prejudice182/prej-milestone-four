from .models import Category


def category_list(request):
    '''
    Returns categories as context so navbar can display in dropdown
    '''
    categories = Category.objects.all()
    return {'categories': categories}
