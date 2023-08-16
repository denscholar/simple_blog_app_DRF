from django.urls import path
from . import views

urlpatterns = [
    path("homepage/", views.list_post, name="posts"),
    path("post_detail/<int:pk>/", views.post_detail, name="post_detail"),
    path("update/<int:pk>/", views.update_post, name="post_update"),
    path("delete/<int:pk>/", views.delete_post, name="post_delete"),
]
