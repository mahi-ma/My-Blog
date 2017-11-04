from rest_framework.serializers import ModelSerializer
from .models import post


class postSerializer(ModelSerializer):
    class Meta:
        model=post
        fields = [
            'title',
            'description',
        ]