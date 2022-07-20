from django.http import HttpResponse, HttpResponseRedirect  # it allows us to get the response from a server
from django.urls import reverse
from django.shortcuts import render
import math
# Create your views here.


def get_rectangle_area(request, width: int, height: int):

    # square = width * height
    # return HttpResponse(f"Площадь прямоугольника размером {height}x{width} равна {square}")
    return render(request, "geometry/rectangle.html")


def get_square_area(request, width: int):

    # square = width**2
    # return HttpResponse(f"Площадь квадрата размером {width}x{width} равна {square}")
    return render(request, "geometry/square.html")


def get_circle_area(request, radius):

    # square = math.pi * radius**2
    # return HttpResponse(f"Площадь круга с радиусом {radius} равна {square}")
    return render(request, "geometry/circle.html")


def get_rectangle_area_redir(request, width: int, height: int):

    redirect_url = reverse("rec-name", args=(width, height))
    # To know the route of redirect go to the main urls.py(in my_page directory in that case)
    return HttpResponseRedirect(redirect_url)


def get_square_area_redir(request, width: int):

    redirect_url = reverse("square-name", args=(width,))
    return HttpResponseRedirect(redirect_url)


def get_circle_area_redir(request, radius: int):

    redirect_url = reverse("circle-name", args=(radius, ))
    return HttpResponseRedirect(redirect_url)