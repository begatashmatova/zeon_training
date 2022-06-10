# import serializer from rest_framework
from rest_framework import serializers
  
# import model from models.py
from .models import Collection
from .models import Post
  
# Create a model serializer 
class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Collection
        fields = ('id', 'title', 'photo')
        

class PostSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'photo1', 'photo2', 'photo3')

