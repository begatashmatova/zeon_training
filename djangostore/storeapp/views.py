from django.shortcuts import render
from rest_framework import viewsets

# import local data
from .serializers import CollectionSerializer
from .models import Collection
from .pagination import CustomPageNumberPagination

# create a viewset
class CollectionViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = Collection.objects.all()
	pagination_class = CustomPageNumberPagination
	# specify serializer to be used
	serializer_class = CollectionSerializer
