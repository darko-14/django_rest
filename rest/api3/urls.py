from django.urls import path
from .views import TruckAPIView, TruckDetailsAPIView

urlpatterns = [
    path('', TruckAPIView.as_view()),
    path('<int:id>', TruckDetailsAPIView.as_view()),
]