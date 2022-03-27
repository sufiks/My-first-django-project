from django.urls import path
from . import views as zodiac

urlpatterns = [
    path('', zodiac.index),
    path('<int:my_zodac>', zodiac.inf_for_zodiac_by_number),
    path('<str:my_zodac>', zodiac.inf_for_zodiac,name='horoscope_name'),
    path('types', zodiac.Types_elements),

]