from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer


# listing and creating a post request
@api_view(http_method_names=["GET", "POST"])
def list_post(request):
    posts = Post.objects.all()

    if request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "post created successfully",
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #
    serializer = PostSerializer(posts, many=True)
    response = {"message": "all posts", "data": serializer.data}
    return Response(data=response, status=status.HTTP_200_OK)


# getting a single post by id and deleting a post
@api_view(http_method_names=["GET", "DELETE"])
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    serializer = PostSerializer(instance=post)
    response = {"message": "post retrieved successfully", "data": serializer.data}
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["PUT"])
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = request.data
    serializer = PostSerializer(instance=post, data=data)

    if serializer.is_valid():
        serializer.save()
        response = {"message": "post updated successfully"}
        return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["DELETE"])
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    response = {"message": "post deleted successfully"}
    return Response(data=response, status=status.HTTP_200_OK)
