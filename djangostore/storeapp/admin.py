from django.contrib import admin
from .models import Benefit
from .models import Collection
from .models import Post
from .models import News
from .models import PublicOffer
from .models import MainPage

from .models import Product
from .models import ProductImage

# Register your models here.
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')

admin.site.register(Benefit, BenefitAdmin)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo')

admin.site.register(Collection, CollectionAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photo1', 'photo2', 'photo3')

admin.site.register(Post, PostAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photo')

admin.site.register(News, NewsAdmin)

class PublicOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(PublicOffer, PublicOfferAdmin)

class MainPageAdmin(admin.ModelAdmin):
    list_display = ('link', 'photo')

admin.site.register(MainPage, MainPageAdmin)


class ProductInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    max_num = 8

class ProductAdmin(admin.ModelAdmin):
    list_display = ('item', 'title','collection', 'description', 'price', 'discount', 'old_price', 'size', 'size_count', 'hits', 'novelty', 'favorite', 'fabric_composition', 'fabric')
    inlines = [
        ProductInline,
    ]

admin.site.register(Product, ProductAdmin)

