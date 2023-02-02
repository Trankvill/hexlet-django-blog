"""hexlet_django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # <- добавлен include
from hexlet_django_blog import views

urlpatterns = [
    path('', views.index), # <- добавляем новое правило обработки главной страницы - назначение обработчиком главной страницы вьюху views.index
    path('about/', views.about), # <- добавляем маршрут about/ вьюху и шаблон
    path('article/', include('hexlet_django_blog.article.urls')),  # <- добавляем путь в urls.py основного пакета путь, включающий в себя вьюху подпакета, которая описана путём до urls.py, содержащегося в подпакете нового приложения
    path('admin/', admin.site.urls),
]
