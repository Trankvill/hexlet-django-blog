from django.shortcuts import render

# Create your views here.

from hexlet_django_blog.article.apps import ArticleConfig


def index(request):
    return render(request, 'article/index.html', context={
        'app_name': ArticleConfig.name,
        })  # Указываем путь до шаблона в созданном приложении(оно уже видит дирректорию templates, поэтому в пути указываем дирректорию article(которая находится внутри templates) и шаблон html. Также указываем имя приложения ссылаясь на name расположенное в apps.py(/article)
