from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer


class PostViewset(viewsets.ModelViewSet):
    # def list(self, request, *args, **kwargs):
    #     queyset = Post.objects.all()
    #     serializer = PostSerializer(instance=queyset, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    # def retrieve(self, request, pk=None):
    #     post = get_object_or_404(Post, pk=pk)
    #     serializer = PostSerializer(instance=post)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    # this provides all CRUD functionality
    queryset = Post.objects.all()
    serializer_class = PostSerializer













# # Generic APIVIEW
# class PostListCreateView(
#     generics.GenericAPIView,
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
# ):
#     """
#     View for creating and listing post
#     """

#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class PostRetrieveUpdateDelete(
#     generics.GenericAPIView,
#     mixins.DestroyModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
# ):
#     """
#     View for retrieving, updating and deleting post
#     """

#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# listing and creating a post request
# class PostListCreate(APIView):
#     """
#     View for creating and listing post
#     """
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         response = {"message": "all posts", "data": serializer.data}
#         return Response(data=response, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "message": "post created successfully",
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class PostRetrieveUppdateAPIView(APIView):
#     def get(self, request, id):
#         post = get_object_or_404(Post, id=id)
#         serializer = PostSerializer(post)
#         respose = {
#             "message": "post retrieved successfully",
#             "data": serializer.data,
#         }
#         return Response(data=respose, status=status.HTTP_200_OK)

#     def put(self, request, id):
#         post = get_object_or_404(Post, id=id)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "message": "post updated successfully",
#             }
#             return Response(data=response, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         post = get_object_or_404(Post, id=id)
#         post.delete()
#         response = {
#             "message": "post deleted successfully",
#         }
#         return Response(data=response, status=status.HTTP_200_OK)


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
