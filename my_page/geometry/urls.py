from django.urls import path
from . import views as geometry

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', geometry.get_rectangle,name='rectangle'),
    path('square/<int:width>', geometry.get_square,name='square'),
    path('circle/<int:radius>', geometry.get_circle,name='circle'),
    path('get_rectangle_area/<int:width>/<int:height>', geometry.get_rectangle_area),
    path('get_square_area/<int:width>', geometry.get_square_area),
    path('get_circle_area/<int:radius>', geometry.get_circle_area),
]