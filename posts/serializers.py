from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # simple validation for model seriaalizers
    title = serializers.CharField(max_length=50)
    class Meta:
        model = Post
        fields = (
            "author",
            "title",
            "content",
            "created_at",
        )

