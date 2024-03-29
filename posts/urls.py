from django.urls import path
from . import views

urlpatterns = [
    # path("homepage/", views.list_post, name="posts"),
    # path("post_detail/<int:pk>/", views.post_detail, name="post_detail"),
    # path("update/<int:pk>/", views.update_post, name="post_update"),
    # path("delete/<int:pk>/", views.delete_post, name="post_delete"),
    # classbased views url endpoints
    path("", views.PostListCreate.as_view(), name="post_list_create"),
    # current user
    path("current_user/", views.PostCurrentUser.as_view(), name="current_user"),
    path("post_detail/<int:id>/", views.PostRetrieveUppdateAPIView.as_view(), name="post_detail"),

    # list posst by user
    path("user/", views.ListOfPostByUser.as_view(), name="list_of_users"),
    # generic viewset endpoints
    # path("", views.PostListCreateView.as_view(), name="list-create"),
    # path("<int:pk>/", views.PostRetrieveUpdateDelete.as_view(), name="retrieve-update-delete"),
]
