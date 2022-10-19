from cgitb import lookup
from urllib.parse import urlparse

from django.urls import path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('api/posts',views.PostsViewSet)
router.register('api/bloggers', views.BloggerViewSet)

posts_router = routers.NestedDefaultRouter(router, 'api/posts', lookup='post')
posts_router.register('images', views.PostsImageViewSet, basename='post-images')

bloggers_router = routers.NestedDefaultRouter(router, 'api/bloggers', lookup='blogger')
bloggers_router.register('images', views.BloggersImageViewSet, basename='blogger-images')

urlpatterns = router.urls + posts_router.urls + bloggers_router.urls