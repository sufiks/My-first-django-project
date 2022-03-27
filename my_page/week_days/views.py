from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

week_dict = {
    'Monday': 'Работать как пони',
    'Tuesday': 'Работать как ишак',
    'Wednesday': 'Пахать как конь',
    'Thursday': 'Притоптывать',
    'Friday': 'Приголубиться об обух',
    'Saturday': 'Фжух фжух',
    'Sunday': 'Вжууууу',
}


def inf_for_day(request, my_day:str):
    description = week_dict.get(my_day)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Неизвестный день - {my_day}')

def inf_for_day_bu_number(request, my_day:int):
    days = list(week_dict)
    if my_day > len(days):
        return HttpResponseNotFound(f'Такого дня не существует - {my_day}')
    name_days = days[my_day-1]
    redirect_url = reverse("name_days", args=[name_days, ])
    return HttpResponseRedirect(f'Сегодня {redirect_url}')

