from django.urls import path
from . import views

urlpatterns = [
    # path("homepage/", views.list_post, name="posts"),
    # path("post_detail/<int:pk>/", views.post_detail, name="post_detail"),
    # path("update/<int:pk>/", views.update_post, name="post_update"),
    # path("delete/<int:pk>/", views.delete_post, name="post_delete"),
    # classbased views url endpoints
    # path("", views.PostListCreate.as_view(), name="post_list_create"),
    # path("post_detail/<int:id>/", views.PostRetrieveUppdateAPIView.as_view(), name="post_detail"),
    # generic viewset endpoints
    path("", views.PostListCreateView.as_view(), name="list-create"),
    path("<int:pk>/", views.PostRetrieveUpdateDelete.as_view(), name="retrieve-update-delete"),
]
