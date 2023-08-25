from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from accounts.serializers import CurrentUserPostSerializer
from .models import Post
from .serializers import PostSerializer


# listing and creating a post request
class PostListCreate(APIView):
    """
    View for creating and listing post
    """

    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title"]

    def get(self, request):
        # user = request.user
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        response = {"message": "all posts", "data": serializer.data}
        return Response(data=response, status=status.HTTP_200_OK)

    def post(self, request: Request):
        user = request.user
        request.data["author"] = user.id  # Associate the user with the post
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "post created successfully",
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostRetrieveUppdateAPIView(APIView):
    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        serializer = PostSerializer(post)
        respose = {
            "message": "post retrieved successfully",
            "data": serializer.data,
        }
        return Response(data=respose, status=status.HTTP_200_OK)

    def put(self, request, id):
        post = get_object_or_404(Post, id=id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "post updated successfully",
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        post = get_object_or_404(Post, id=id)
        post.delete()
        response = {
            "message": "post deleted successfully",
        }
        return Response(data=response, status=status.HTTP_200_OK)


class PostCurrentUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = CurrentUserPostSerializer(instance=user)

        response = {"data": serializer.data}
        return Response(data=response, status=status.HTTP_200_OK)


class ListOfPostByUser(APIView):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title"]

    def get(self, request, *args, **kwargs):
        author = request.user
        posts = Post.objects.filter(author=author)
        serializer = PostSerializer(instance=posts, many=True)

        response = {"posts": serializer.data}
        return Response(data=response, status=status.HTTP_200_OK)
