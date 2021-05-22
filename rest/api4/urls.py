from django.urls import path
from .views import GenericAPIView

urlpatterns = [
    path('', GenericAPIView.as_view()),
    path('<int:pk>', GenericAPIView.as_view()),
]