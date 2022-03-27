from django.urls import path
from . import views as week

urlpatterns = [
    #path('', views.index),
    path('<int:my_day>', week.inf_for_day_bu_number),
    path('<str:my_day>', week.inf_for_day, name='name_days'),
]