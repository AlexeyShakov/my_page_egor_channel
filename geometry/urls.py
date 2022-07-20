from django.urls import path
from . import views  # '.' means that we wanna import from the same folder

urlpatterns = [
    # with this line of code we can get rid of listing all zodiac signs
    path('get_rectangle_area/<int:width>/<int:height>/', views.get_rectangle_area_redir),  # "<>" means parameter in django
    path('get_square_area/<int:width>/', views.get_square_area_redir),  # "<>" means parameter in django
    path('get_circle_area/<int:radius>/', views.get_circle_area_redir),  # "<>" means parameter in django
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area, name="rec-name"),  # "<>" means parameter in django
    path('square/<int:width>/', views.get_square_area, name="square-name"),  # "<>" means parameter in django
    path('circle/<int:radius>/', views.get_circle_area, name="circle-name"),
]