from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from .models import Post
from .serializers import PostSerializer


# listing and creating a post request
class PostListCreate(APIView):
    """
    View for creating and listing post
    """
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        response = {"message": "all posts", "data": serializer.data}
        return Response(data=response, status=status.HTTP_200_OK)
    
    def post(self, request):
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

    


# @api_view(http_method_names=["GET", "POST"])
# def list_post(request):
#     posts = Post.objects.all()

#     if request.method == "POST":
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "message": "post created successfully",
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     #
#     serializer = PostSerializer(posts, many=True)
#     response = {"message": "all posts", "data": serializer.data}
#     return Response(data=response, status=status.HTTP_200_OK)


# # getting a single post by id and deleting a post
# @api_view(http_method_names=["GET", "DELETE"])
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     serializer = PostSerializer(instance=post)
#     response = {"message": "post retrieved successfully", "data": serializer.data}
#     return Response(data=response, status=status.HTTP_200_OK)


# @api_view(http_method_names=["PUT"])
# def update_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     data = request.data
#     serializer = PostSerializer(instance=post, data=data)

#     if serializer.is_valid():
#         serializer.save()
#         response = {"message": "post updated successfully"}
#         return Response(data=response, status=status.HTTP_200_OK)


# @api_view(http_method_names=["DELETE"])
# def delete_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.delete()
#     response = {"message": "post deleted successfully"}
#     return Response(data=response, status=status.HTTP_200_OK)
