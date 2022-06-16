# import serializer from rest_framework
from rest_framework import serializers
  
# import model from models.py
from .models import Collection
from .models import Post
from .models import News
from .models import PublicOffer
from .models import Product
from .models import ProductImage
  
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


class PublicOfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PublicOffer
        fields = ('id', 'title', 'description')


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['color', 'photo']


class ProductSerializer(serializers.ModelSerializer):
    colors = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('item', 'title', 'collection', 'description', 'price', 'discount', 'old_price', 'size', 'size_count', 'fabric', 'fabric_composition', 'hits', 'novelty', 'favorite', 'colors')


class SimilarProductSerializer(serializers.ModelSerializer):
    colors = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'discount', 'old_price', 'size', 'size_count', 'favorite', 'colors')


class ProductCollectionSerializer(serializers.ModelSerializer):
    colors = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'discount', 'old_price', 'size', 'favorite', 'colors')


