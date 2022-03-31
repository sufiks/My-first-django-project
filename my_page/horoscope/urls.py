from django.urls import path
from . import views as zodiac

urlpatterns = [
    path('', zodiac.index),
    path('<int:my_zodac>', zodiac.inf_for_zodiac_by_number),
    path('<str:my_zodac>', zodiac.inf_for_zodiac,name='horoscope_name'),
    path('type/', zodiac.index_type),
    path('<str:type>', zodiac.inf_for_types, name='type_name'),
    path('type/earth', zodiac.earth),
    path('type/air', zodiac.air),
    path('type/water', zodiac.water),
    path('type/fire', zodiac.fire),

]