from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def get_rectangle(request, width: int, height: int):
    return HttpResponse(f'Площадь прямоугольника равна {width * height}')


def get_square(request, width: int):
    return HttpResponse(f'Площадь квадрата равна{width ** 2}')


def get_circle(request, radius: int):
    return HttpResponse(f'Площадь круга равна {3.14 * radius ** 2}')


def get_rectangle_area(request, width: int, height: int):
    return HttpResponseRedirect(reverse('rectangle', args=[width, height]))


def get_square_area(request, width: int):
    return HttpResponseRedirect(reverse(get_square, args=[width]))


def get_circle_area(request, radius: int):
    return HttpResponseRedirect(reverse(get_circle, args=[radius]))
