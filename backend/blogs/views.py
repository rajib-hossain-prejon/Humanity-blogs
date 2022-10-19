from itertools import product
from pprint import pprint
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin 
from .serializers import PostsImageSerializer, PostsSerializer, BloggersSerializer, BloggersImageSerializer
from .models import Posts, Blogger, PostsImage, BloggersImage
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status

# from blogapp.permissions import FullDjangoModelPermissions, IsAdminOrReadOnly, ViewCustomerHistoryPermission

# Create your views here.
class PostsViewSet(ModelViewSet):
  queryset = Posts.objects.prefetch_related('images').all()
  serializer_class = PostsSerializer
#CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet

class PostsImageViewSet(ModelViewSet):
  serializer_class = PostsImageSerializer
  def get_serializer_context(self):
    return {'post_id': self.kwargs['post_pk']}

  def get_queryset(self):
    return PostsImage.objects.filter(post_id=self.kwargs['post_pk'])

class BloggerViewSet(ModelViewSet): 
    queryset = Blogger.objects.all()
    serializer_class = BloggersSerializer
    
    def get_permissions(self):
      if self.request.method == 'GET':
        return [AllowAny()]
      return [IsAuthenticated()]
    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
      (blogger, created) = Blogger.objects.get_or_create(user_id=request.user.id)
      if request.method == 'GET':
        serializer = BloggersSerializer(blogger)
        return Response(serializer.data)
      elif request.method == 'PUT':
        serializer = BloggersSerializer(blogger, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class BloggersImageViewSet(ModelViewSet):
  serializer_class = BloggersImageSerializer
  def get_serializer_context(self):
    return {'blogger_id': self.kwargs['blogger_pk']}

  def get_queryset(self):
    return BloggersImage.objects.filter(blogger_id=self.kwargs['blogger_pk'])

#     pprint(queryset)
    # permission_classes = [IsAdminUser]

    # @action(detail=True, permission_classes=[ViewCustomerHistoryPermission])
    # def history(self, request, pk):
    #     return Response('ok')

    # @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    # def me(self, request):
    #     customer = Blogger.objects.get(
    #         user_id=request.user.id)
    #     if request.method == 'GET':
    #         serializer =BloggersSerializer(Blogger)
    #         return Response(serializer.data)
    #     elif request.method == 'PUT':
    #         serializer = BloggersSerializer(Blogger, data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)