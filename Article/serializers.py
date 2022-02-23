from rest_framework import serializers
from Article.models import Users, Articles


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name', 'username', 'password')


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('title', 'description')
