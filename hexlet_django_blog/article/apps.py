from django.apps import AppConfig


class ArticleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hexlet_django_blog.article' # <- указание полного пути к новому приложению(болванке/будущему приложению)
