from django.urls import path
from .views import TruckAPIView, TrucDetailskAPIView

urlpatterns = [
    path('', TruckAPIView.as_view()),
    path('<int:id>', TrucDetailskAPIView.as_view()),
]