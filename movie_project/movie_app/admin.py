from django.contrib import admin, messages
from .models import Movie
from django.db.models import QuerySet

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name','rating','currency','budget', 'rating_status']
    list_editable = ['rating','currency','budget']
    ordering = ['rating','name']
    list_per_page = 10
    actions = ['set_dollars','set_euro']
    search_fields = ['name__startswitch','rating']


    @admin.display(ordering='rating', description='Status')
    def rating_status(self, mov:Movie):
        if mov.rating < 50:
            return 'Зачем это смотреть?'
        elif mov.rating < 70:
            return 'Разок можно глянуть'
        elif mov.rating <= 85:
            return 'Зачет'
        return 'Топчик'

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self,request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в Евро')
    def set_euro(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'Было обновлено {count_updated} записей',
            messages.ERROR
        )