from django.shortcuts import render
from rest_framework import viewsets

# import local data
from .serializers import CollectionSerializer, PostSerializer, NewsSerializer
#from .serializers import PostSerializer
from .pagination import CustomPageNumberPagination

from .models import Collection
from .models import Post
from .models import News

# create a viewset
class CollectionViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = Collection.objects.all()
	pagination_class = CustomPageNumberPagination
	# specify serializer to be used
	serializer_class = CollectionSerializer


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class NewsViewSet(viewsets.ModelViewSet):
	queryset = News.objects.all()
	pagination_class = CustomPageNumberPagination
	serializer_class = NewsSerializer

