from django.contrib import admin
from django.contrib.admin import DateFieldListFilter  #  импортируем фильтрацию полей

# Register your models here.
from .models import Article

@admin.register(Article)  # добавление декоратора, позволяющего связать модель с классом и провести регистрацию модели в разделе администратора
class ArticleAdmin(admin.ModelAdmin):
    #  добавляем отображение в списке статей даты публикации и фильтрацию по данному полю
    list_display = ('name', 'timestamp')  # перечисляем поля, отображаемые в таблице списка статей
    search_fields = ['name', 'body']  # добавление поисковой формы (класс ArticleAdmin) по соответсвующим полям, указанным в списке
    list_filter = (('timestamp', DateFieldListFilter),)  # перечисляем поля для фильтрации


#admin.site.register(Article, ArticleAdmin)  # добавление класса с поисковой формой. Закадрил! Т.к. при запуске сервера выдало ошибку о том, что ArticleAdmin (который был раннее добавлен) уже существует. При добавлении нового класса раскадрить и запустить сервер!
