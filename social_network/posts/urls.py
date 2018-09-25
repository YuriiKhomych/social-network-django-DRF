from django.urls import path
from .views import PostCreateAPIView, AllPostAPIView

urlpatterns = [
    path('posts/', AllPostAPIView.as_view()),
    path('posts/create/', PostCreateAPIView.as_view()),
]
