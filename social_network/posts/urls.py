from django.urls import path
from .views import PostCreateAPIView, AllPostAPIView, PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', AllPostAPIView.as_view()),
    path('create/', PostCreateAPIView.as_view()),
    path('<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view()),
]
