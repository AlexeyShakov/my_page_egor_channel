from django.urls import path
from . import views  # '.' means that we wanna import from the same folder

""" 
route handling implemented from top to bottom. So the order matters. So if the script doesn't find matches with
int converter it goes further and check str converter
"""
urlpatterns = [
    # with this line of code we can get rid of listing all zodiac signs
    path('', views.index, name="horoscope-index"),
    path('type', views.list_nature),
    path('type/<nature>', views.get_nature, name="natures_name"),
    path('<int:zodiac_sign>', views.get_info_about_zodiac_by_number),  # "<>" means parameter in django
    path('<str:zodiac_sign>', views.get_info_about_zodiac, name="horoscope-name"),  # "<>" means parameter in django
]