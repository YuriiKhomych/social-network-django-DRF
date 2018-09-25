from django.urls import path
from .views import CreateUserAPIView, LoginUserAPIView, RetrieveUpdateUserAPI

urlpatterns = [
    path('users/create/', CreateUserAPIView.as_view()),
    path('users/get_token/', LoginUserAPIView.as_view()),
    path('users/update/', RetrieveUpdateUserAPI.as_view()),
]