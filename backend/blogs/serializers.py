from dataclasses import field
from math import trunc
from rest_framework import serializers
from .models import Posts, Blogger, PostsImage, BloggersImage

class PostsImageSerializer(serializers.ModelSerializer):

  def create(self, validated_data):
    post_id = self.context['post_id']
    return PostsImage.objects.create(post_id=post_id, **validated_data)

  class Meta:
    model = PostsImage
    fields = ['id', 'image']

class PostsSerializer(serializers.ModelSerializer):
 
 images = PostsImageSerializer(many = True, read_only = True)

 class Meta:
  model = Posts
  fields = ['id', 'blogger', 'description', 'date', 'images']

class BloggersImageSerializer(serializers.ModelSerializer):

  def create(self, validated_data):
    blogger_id = self.context['blogger_id']
    return BloggersImage.objects.create(blogger_id=blogger_id, **validated_data)

  class Meta:
    model = BloggersImage
    fields = ['id', 'image']

class BloggersSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Blogger
        fields = ['id', 'user_id', 'phone', 'birth_date', 'membership', 'images']
