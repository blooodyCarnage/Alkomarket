from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Контакты', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Виски', 'category': 'whiskey',
     'content': 'Шотландский виски - это крепкий алкогольный напиток, производимый из ячменя. Выдерживается в дубовых бочках не менее 3 лет.',
     'is_published': True},
    {'id': 2, 'title': 'Вино', 'category': 'wine',
     'content': 'Красное вино изготавливается из темных сортов винограда. Обладает богатым вкусом и ароматом.',
     'is_published': True},
    {'id': 3, 'title': 'Пиво', 'category': 'beer',
     'content': 'Традиционный слабоалкогольный напиток, получаемый путем брожения солода.',
     'is_published': False},
    {'id': 4, 'title': 'Коньяк', 'category': 'cognac',
     'content': 'Французский коньяк производится в регионе Коньяк из определенных сортов винограда.',
     'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Крепкий алкоголь'},
    {'id': 2, 'name': 'Вино'},
    {'id': 3, 'name': 'Пиво'},
    {'id': 4, 'name': 'Ликеры'},
]


def index(request):
    data = {
        'title': 'главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
    }
    return render(request, 'alko/index.html', context=data)


def about(request):
    data = {
        'title': 'о сайте',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'alko/about.html', context=data)


def show_post(request, post_id):
    post = None
    for p in data_db:
        if p['id'] == post_id:
            post = p
            break

    if not post:
        raise Http404("Статья не найдена")

    data = {
        'title': post['title'],
        'menu': menu,
        'post': post,
    }
    return render(request, 'alko/post.html', context=data)


def contact(request):
    return HttpResponse("Обратная связь: alkomarket@example.com")


def login(request):
    return HttpResponse("Страница авторизации")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def archive(request, year):
    if year > 2024:
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def categories_by_slug(request, cat_slug):
    # Словарь с названиями категорий
    categories_names = {
        'whiskey': 'Виски',
        'wine': 'Вино',
        'beer': 'Пиво',
        'cognac': 'Коньяк',
        'vodka': 'Водка',
    }

    # Фильтруем товары по категории
    filtered_posts = [p for p in data_db if p.get('category') == cat_slug]

    data = {
        'title': categories_names.get(cat_slug, cat_slug),
        'category_name': categories_names.get(cat_slug, cat_slug),
        'products': filtered_posts,
        'menu': menu,
    }
    return render(request, 'alko/category.html', data)