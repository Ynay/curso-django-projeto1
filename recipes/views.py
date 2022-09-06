from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = get_list_or_404(              # Usado para fazer uma busca em uma lista se caso não for encontrado algo ele irá retornar um erro 404
        Recipe.objects.filter(              # Filtragem dos dados pelos campos
            category__id=category_id,       # Filtragem pelo campo id dos Objects

            # Filtragem pelo campo publicado se for igual a verdadeiro(TRUE)
            is_published=True,
        ).order_by('-id')                   # Ordanando os dados filtrados pelo ID pela ordem descrescente
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | '
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
