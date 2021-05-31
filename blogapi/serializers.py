from blog.models import Post
from django.contrib.auth.models import User
from rest_framework import serializers

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [ 'id','author','title','body','url']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name', 'email' ,'date_joined','url']