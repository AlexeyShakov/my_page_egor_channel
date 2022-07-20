from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect  # it allows us to get the response from a server
from django.urls import reverse
# Create your views here.

days = {
    'monday': 'в понедельник я жалею себя',
    'tuesday': 'во вторник - глазею в пропасть',
    'wednesday': 'в среду решаю проблему мирового голода (никому не говорите)',
    'thursday ': 'в четверг - зарядка',
    'friday ': 'ужин с собой, нельзя снова его пропускать',
    'saturday ': 'в субботу - борьба с презрением к себе',
    'sunday ': 'в воскресенье - иду на рождество'
}


def get_the_day_of_the_week(request, day):

    if day in days:
        return HttpResponse(days[day])
    else:
        return HttpResponseNotFound(f"Неизвестный день недели - {day}")


def get_the_day_of_the_week_by_number(request, day: int):

    days_list = list(days.keys())
    if day > len(days_list):
        return HttpResponse(f"Неверный номер дня - {day}")
    day_name = days_list[day - 1]
    redirect_url = reverse("week-name", args=(day_name,))
    return HttpResponseRedirect(redirect_url)


def greeting(request):

    return render(request, 'weeks/greeting.html')
