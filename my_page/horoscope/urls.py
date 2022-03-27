from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:my_zodac>', views.inf_for_zodiac_by_number),
    path('<str:my_zodac>', views.inf_for_zodiac,name='horoscope_name'),

]