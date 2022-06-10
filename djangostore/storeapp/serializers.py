# import serializer from rest_framework
from rest_framework import serializers
  
# import model from models.py
from .models import Collection
  
# Create a model serializer 
class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Collection
        fields = ('id', 'title', 'photo')