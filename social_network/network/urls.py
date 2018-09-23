from django.urls import path
from .views import CreateUserAPIView, LoginUserAPIView, RetrieveUpdateUserAPI

urlpatterns = [
    path('user/create/', CreateUserAPIView.as_view()),
    path('user/get_token/', LoginUserAPIView.as_view()),
    path('user/update/', RetrieveUpdateUserAPI.as_view()),
]