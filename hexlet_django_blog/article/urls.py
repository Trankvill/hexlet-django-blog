from django.urls import path


from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleCommentsView, ArticleFormCreateView, ArticleFormEditView, ArticleFormDestroyView


urlpatterns = [
        path('', IndexView.as_view(), name='articles'),
        path('<int:id>/', ArticleView.as_view(), name='article'),
        path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view()),
        path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
        path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_edit'),
        path('<int:id>/delete/', ArticleFormDestroyView.as_view(), name='articles_destroy'),
]
