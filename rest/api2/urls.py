from django.urls import path
from .views import car_detail, car_list

urlpatterns = [
    path('', car_list),
    path('<int:pk>', car_detail),
]