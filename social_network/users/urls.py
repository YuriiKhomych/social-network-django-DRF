from django.urls import path
from .views import CreateUserAPIView, LoginUserAPIView, RetrieveUpdateUserAPI

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('login/', LoginUserAPIView.as_view()),
    path('update/', RetrieveUpdateUserAPI.as_view()),
]
