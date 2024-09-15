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
from .models import CartItem
from .models import Cart
from .models import Customer
from .models import Order
from .models import ShippingAddress


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


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('product', 'date_added', 'quantity', 'get_total')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('user', 'name', 'email')


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = (
            'customer',
            'address',
            'city',
            'country',
            'order'
        )


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'date_added', 'id']


class CartSerializer(serializers.ModelSerializer):
    cartitems = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = (
            'id',
            'customer',
            'date_ordered',
            'get_cart_total',
            'cartitems'
        )


class OrderHistorySerializer(serializers.ModelSerializer):
    cartitems = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'customer',
            'date_ordered',
            'get_cart_total',
            'cartitems'
        )