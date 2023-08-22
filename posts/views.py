from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer


# Generic APIVIEW
class PostListCreateView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
):
    """
    View for creating and listing post
    """

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRetrieveUpdateDelete(
    generics.GenericAPIView,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    """
    View for retrieving, updating and deleting post
    """

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)