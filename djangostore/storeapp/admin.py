from django.contrib import admin
from .models import Benefit
from .models import Collection
from .models import Post
from .models import News
from .models import PublicOffer
from .models import MainPage
from .models import Product
from .models import ProductImage
from .models import Help
from .models import HelpImage
from .models import Call
from .models import Footer
from .models import ContactInfo
from .models import CartItem
from .models import Customer
from .models import Cart
from .models import ShippingAddress
from .models import Order

class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

admin.site.register(Benefit, BenefitAdmin)


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo')

admin.site.register(Collection, CollectionAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photo1', 'photo2', 'photo3')

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

admin.site.register(Post, PostAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photo')

admin.site.register(News, NewsAdmin)


class PublicOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

admin.site.register(PublicOffer, PublicOfferAdmin)


class MainPageAdmin(admin.ModelAdmin):
    list_display = ('link', 'photo')

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

admin.site.register(MainPage, MainPageAdmin)


class ProductInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    max_num = 8


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'item',
        'title',
        'collection',
        'description',
        'price',
        'discount',
        'old_price',
        'size',
        'size_count',
        'hits',
        'novelty',
        'favorite',
        'fabric_composition',
        'fabric'
    )
    inlines = [
        ProductInline,
    ]
admin.site.register(Product, ProductAdmin)


class HelpAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')

admin.site.register(Help, HelpAdmin)


class HelpImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
    max_num = 1

admin.site.register(HelpImage, HelpImageAdmin)


class CallAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'call_type', 'call_date', 'call_status')
    list_filter = ('call_status',)
    search_fields = ['name', 'number']

admin.site.register(Call, CallAdmin)


class FooterInline(admin.TabularInline):
    model = ContactInfo
    extra = 0
    max_num = 8


class FooterAdmin(admin.ModelAdmin):
    list_display = (
        'description', 'header_logo', 'footer_logo', 'header_number'
    )
    inlines = [
        FooterInline,
    ]

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

admin.site.register(Footer, FooterAdmin)


class CartItemAdmin(admin.ModelAdmin):
    list_display = [
        'product', 'color', 'photo', 'quantity', 'get_total', 'size', 'final_price', 'old_price', 'price', 'cart'
    ]

admin.site.register(CartItem, CartItemAdmin)


class ShippingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ShippingAddress._meta.get_fields()]

admin.site.register(ShippingAddress, ShippingAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'user')

admin.site.register(Customer, CustomerAdmin)


class ShippingInLine(admin.StackedInline):
    model = ShippingAddress
    extra = 0
    max_num = 8


class CartItemInLine(admin.TabularInline):
    model = CartItem
    extra = 0
    max_num = 8


class OrderAdmin(admin.ModelAdmin):
    list_display = list_display = ['id', 'customer', 'date_ordered', 'get_cart_total', 'get_cart_items', 'get_products_count', 'get_discount_amount', 'get_final_price', 'item_list']
    
    inlines = [
        CartItemInLine
    ]

admin.site.register(Cart, OrderAdmin)


class OrderHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'old_price', 'final_price', 'products_count', 'items_count', 'discount')

    inlines = [
        ShippingInLine, CartItemInLine
    ]

admin.site.register(Order, OrderHistoryAdmin)



