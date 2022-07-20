from django.urls import path
from . import views  # '.' means that we wanna import from the same folder

urlpatterns = [
    path('<int:day>', views.get_the_day_of_the_week_by_number),
    path('<str:day>', views.get_the_day_of_the_week, name="week-name"),
    path('', views.greeting),
    # path('monday/', views.monday),  # after ',' we have to put the view to the URL
    # path('tuesday/', views.tuesday),
]