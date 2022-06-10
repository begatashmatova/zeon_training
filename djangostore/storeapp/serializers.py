# import serializer from rest_framework
from rest_framework import serializers
  
# import model from models.py
from .models import Collection
from .models import Post
from .models import News
  
# Create a model serializer 
class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'title', 'photo')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'photo1', 'photo2', 'photo3')


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'photo')


