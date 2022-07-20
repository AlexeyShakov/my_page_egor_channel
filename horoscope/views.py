from django.shortcuts import render # can create Http response and convert HTML template to string at once
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound  # it allows us to get the response from a server
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

nature_dict = {
    "fire": ("aries", "leo", "sagittarius"),
    "earth": ("taurus", "virgo", "capricorn"),
    "air": ("gemini", "libra", "aquarius"),
    "water": ("cancer", "scorpio", "pisces"),
               }




signs = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}


# the function has to take one argument. Often this argument is called 'request'
# the function which allows us to use dinamic URLs. To addition to request we have to send
# parameter(zodiac_sign) from urlpatterns. Dinamic URLs allow us to reduce the amount of code

""" 
We can show our pages not by name of zodiac signs but by listing numbers. For it we have to add a line
to the config with indication to the converter format(int, str, etc)
"""


def get_info_about_zodiac(request, zodiac_sign: str):

    # # render_to_string() convers everything from HTML template to string format
    # response = render_to_string("horoscope/info_zodiac.html")
    description = signs.get(zodiac_sign)
    data = {
        "zodiac_description": description,
        "sign": zodiac_sign
    }
    return render(request, "horoscope/info_zodiac.html", context=data)


def get_info_about_zodiac_by_number(request, zodiac_sign: int):
    zodiacs = list(signs)
    if zodiac_sign > len(zodiacs):
        return HttpResponse(f"Неправильный порядковый номер знака зодиака - {zodiac_sign}")
    name_zodiac = zodiacs[zodiac_sign - 1]
    """ 
    Reverse function is needed for getting base URL from the url.py of the main directory(in this case "my_page").
    If we don't use it and send the URL to HttpResponseRedirect by hand then we can get in trouble if the URL 
    changes often. So the reverse function enables us to change the base part of URL automatically 
    """
    redirect_url = reverse("horoscope-name", args=(name_zodiac,))
    # HttpResponseRedirect we can redirect our request to another URL but this URL must be handle by a function
    # otherwise there`ll be a mistake
    # To know the route of redirect go to the main urls.py(in my_page directory in that case)
    return HttpResponseRedirect(redirect_url)


def index(request):

    zodiacs = list(signs)
    # f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
    context = {
        "zodiacs": zodiacs
    }
    return render(request, "horoscope/index.html", context=context)


def list_nature(request):

    nature_list = list(nature_dict)
    # f"<li> <a href='{redirect_url}'>{nature.title()} </a></li>"
    elements = ""
    for nature in nature_list:
        redirect_url = reverse("natures_name", args=[nature])
        elements += f"<li> <a href='{redirect_url}'>{nature.title()} </a></li>"
    response = f""" 
    <ul>
    {elements}
    </ul>
    """
    return HttpResponse(response)


def get_nature(request, nature):

    # Check that the element(стихия) exists
    if nature in nature_dict:
        tup_elements = ""
        # Iterate through elements in dictionary values(a tuple)
        for element in nature_dict[nature]:
            redirect_path = reverse("horoscope-name", args=[element])
            tup_elements += f"<li> <a href='{redirect_path}'>{element.title()} <a> </li>"
        response = f""" 
        <ul>
        {tup_elements}
        <ul>
        """
        return HttpResponse(response)
    else:
        return HttpResponseNotFound(f"Вы ввели неверную стихию - {nature}")









