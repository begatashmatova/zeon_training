from rest_framework import serializers
from .models import Collection
from .models import Post
from .models import News
from .models import PublicOffer
from .models import Product
from .models import ProductImage
from .models import Help
from .models import HelpImage
from .models import MainPage
from .models import Benefit
from .models import ContactInfo
from .models import Footer

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
        fields = (
            'item',
            'title',
            'collection',
            'description',
            'price',
            'discount',
            'old_price',
            'size',
            'size_count',
            'fabric',
            'fabric_composition',
            'hits',
            'novelty',
            'favorite',
            'colors'
        )


class SimilarProductSerializer(serializers.ModelSerializer):
    colors = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'price',
            'discount',
            'old_price',
            'size',
            'size_count',
            'favorite',
            'colors'
        )


class ProductCollectionSerializer(serializers.ModelSerializer):
    colors = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'price',
            'discount',
            'old_price',
            'size',
            'favorite',
            'colors'
        )


class FavoriteProductSerializer(serializers.ModelSerializer):
    colors = ProductImageSerializer(many=True, read_only=True)
    favs = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'price',
            'discount',
            'old_price',
            'size',
            'favorite',
            'colors'
        )

    def get_favs(self, obj):
        return {"favs": self.context.get("favs")}


class HelpImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpImage
        fields = ['image', ]


class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ['question', 'answer']


class MainPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MainPage
        fields = ('link', 'photo')


class BenefitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Benefit
        fields = ('icon', 'title', 'description')


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = [
            'network_type',
            'contact'
        ]


class FooterSerializer(serializers.ModelSerializer):
    contacts = ContactInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Footer
        fields = (
            'description',
            'header_logo',
            'footer_logo',
            'header_number',
            'contacts'
        )
