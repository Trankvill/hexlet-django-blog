from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import CommentArticleForm, ArticleForm
from django.forms import ModelForm

# Create your views here.

from hexlet_django_blog.article.models import Article


class IndexView(View):


    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]  # Добавление содержимого подключенной модели и вывод первых 15-ти статей, находящихся в таблице
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):


    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


class ArticleCommentsView(View):

    
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=kwargs['id'], article__id=kwargs['article_id'])
        return render(request, 'articles/show.html', context={
            'comment': comment,
        })


class CommentArticleView(View):


    def get(self, request, *args, **kwargs):
        form = CommentArticleForm() # Создаём экземпляр нашей формы
        return render(request, 'comment.html', {'form': form}) # Передаём нашу форму в контексте


    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST) # Получаем данные формы из запроса
        if form.is_valid(): # Проверяем данных формы на корректность
            comment = Comment(
                    name = form.cleaned_data['content'], # Получаем очищенные данные из поля name
                    )
            comment.save()


class ArticleFormCreateView(View):


    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})


    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid(): # Если данные корректные, то сохраняем данные формы
            form.save()
            return redirect('articles') # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        return render(request, 'articles/create.html', {'form': form})


class ArticleFormEditView(View):


    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article) # Аргумент instance - для заполнения формы данными из модели
        return render(request, 'articles/update.html', {'form': form, 'article_id':article_id})


    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')


        return render(request, 'update.html', {'form': form, 'article_id':article_id})


class ArticleFormDestroyView(View):


    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('articles')
