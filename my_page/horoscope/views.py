from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}


type_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],

}

def inf_for_types(request, type: str):
    descrip=type_dict.get(type)
    return HttpResponse(descrip)

def index_type(request):
    types = list(type_dict)
    li_elements = ''
    for sign in types:
        redirect_type = reverse("type_name", args=[sign])
        li_elements += f"<li> <a href='{redirect_type}'>{sign} </a> </li>"
    responce = f"""
    <ol>
        {li_elements}
    </ol>
    """
    return HttpResponse(responce)


def earth(request):
    earth = f"""
                <ol>
                    <li> <a href='earth'> {'taurus'} </a> </li>
                    <li> <a href='air'> {'virgo'} </a> </li>
                    <li> <a href='water'> {'capricorn'} </a> </li>
                </ol>
            """
    return HttpResponse(earth)

def air(request):
    air = f"""
                 <ol>
                     <li> <a href='earth'> {'gemini'} </a> </li>
                     <li> <a href='air'> {'libra'} </a> </li>
                     <li> <a href='water'> {'aquarius'} </a> </li>                     
                 </ol>
                 """
    return HttpResponse(air)

def water(request):
    water = f"""
                 <ol>
                     <li> <a href='earth'> {'cancer'} </a> </li>
                     <li> <a href='air'> {'scorpio'} </a> </li>
                     <li> <a href='air'> {'pisces'} </a> </li>                     
                 </ol>
                 """
    return HttpResponse(water)


def fire(request):
    fire = f"""
                    <ol>
                         <li> <a href='earth'> {'aries'} </a> </li>
                         <li> <a href='air'> {'leo'} </a> </li>
                         <li> <a href='air'> {'sagittarius'} </a> </li>
                     </ol>
            """
    return HttpResponse(fire)

def index(request):
    zodiacs = list(zodiac_dict)
    #f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
    context = {
        'zodiacs': zodiacs
    }
    return render(request, 'horoscope/index.html', context = context)

def inf_for_zodiac(request, my_zodac: str):
    return render(request,'horoscope/info_zodiac.html')



def inf_for_zodiac_by_number(request, my_zodac: int):
    zodiacs = list(zodiac_dict)
    if my_zodac > len(zodiacs):
        return HttpResponseNotFound(f'неверный знак зодиака - {my_zodac}')
    name_zodiacs = zodiacs[my_zodac-1]
    return HttpResponseRedirect(reverse("horoscope_name", args=[name_zodiacs, ]))



