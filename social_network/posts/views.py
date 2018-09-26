from .models import Post
from .serializers import PostCreateSerializer, AllPostSerializer, PostUpdateSerializer

from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination


class AllPostAPIView(ListAPIView):
    """
    This view will return response with full articles
    (title, body, data, author, liked_by),
    but divided into 10 users objects at the one response.
    Used limit and offset.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = AllPostSerializer
    pagination_class = LimitOffsetPagination


class PostCreateAPIView(ListCreateAPIView):
    """
    This view will check input user unique title name and then,
    if data is valid, create new article
    and return success message
    """
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        # The request user is set as author automatically.
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """This view aim to retrieve(get), create(put), update(patch) and
     delete(delete) post by id"""
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
