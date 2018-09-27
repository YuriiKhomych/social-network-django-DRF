from django.urls import path
from .views import PostCreateAPIView, AllPostAPIView, \
    PostRetrieveUpdateDestroyAPIView, PostLikeAPIView

urlpatterns = [
    path('', AllPostAPIView.as_view()),
    path('create/', PostCreateAPIView.as_view()),
    path('<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view()),
    path('like/<int:post_id>/', PostLikeAPIView.as_view()),
]
