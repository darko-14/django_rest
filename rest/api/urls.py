from django.urls import path
from .views import member_list, member_detail

urlpatterns = [
    path('', member_list),
    path('<int:pk>', member_detail),
]