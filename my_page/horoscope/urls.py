from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:my_zodac>/', views.inf_for_zodiac_by_number, name="horoscope_name"),
    path('<str:my_zodac>/', views.inf_for_zodiac),

]