from rest_framework import serializers
from django.conf import settings

from core.abstract.serializers import AbstractSerializer
from core.user.models import User

class UserSerializer(AbstractSerializer):
    posts_count = serializers.SerializerMethodField()

    def get_posts_count(self, instance):
        return instance.post_set.all().count()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # If avatar is missing or None, set a default value
        avatar = instance.avatar.url if instance.avatar else settings.DEFAULT_AVATAR_URL
        
        request = self.context.get("request")
        
        if request and settings.DEBUG:
            # Only build absolute URI if in DEBUG mode and request is available
            avatar = request.build_absolute_uri(avatar)

        representation["avatar"] = avatar
        return representation

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "name",
            "first_name",
            "last_name",
            "bio",
            "avatar",
            "email",
            "is_active",
            "created",
            "updated",
            "posts_count",
        ]
        read_only_field = ["is_active"]
