from django.contrib.auth.models import User
from django.db.models import fields
from blog.models import Post
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'created_on', 'updated_on', 'status', 'content' ]
