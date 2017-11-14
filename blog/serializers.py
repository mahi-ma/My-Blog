from rest_framework.serializers import ModelSerializer
from .models import Post

class postSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields = [
            'title',
            'description',
        ]