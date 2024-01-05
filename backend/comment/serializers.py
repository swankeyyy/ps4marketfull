from rest_framework import serializers
from .models import Comment
from users.models import User



class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class CommentSerializer(serializers.ModelSerializer):
    user = UserCommentSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


