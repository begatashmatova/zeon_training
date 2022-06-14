from django.db import models
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField

# Benefits
class Benefit(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    icon = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'benefit'
        verbose_name = 'Benefit'
        verbose_name_plural = 'Benefits'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title


# Collection
class Collection(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    class Meta:
        db_table = 'collection'
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title


# Post
class Post(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = RichTextField(blank=True, null=True)
    photo1 = models.ImageField(null=True, blank=True, upload_to='images/')
    photo2 = models.ImageField(null=True, blank=True, upload_to='images/')
    photo3 = models.ImageField(null=True, blank=True, upload_to='images/')
    class Meta:
        db_table = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title


# News
class News(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = RichTextField(blank=True, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    class Meta:
        db_table = 'news'
        verbose_name = 'News'
        verbose_name_plural = 'News'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title


# Public Offer
class PublicOffer(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = RichTextField(blank=True, null=True)
    class Meta:
        db_table = 'publicoffer'
        verbose_name = 'Publicoffer'
        verbose_name_plural = 'Public offers'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title



# Main Page
class MainPage(models.Model):
    link = models.CharField(db_column='link', max_length=100, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    class Meta:
        db_table = 'mainpage'
        verbose_name = 'Main page'
        verbose_name_plural = 'Main pages'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title


# Product
class Product(models.Model):
    item = models.CharField(db_column='item', max_length=100, blank=True)
    title = models.CharField(db_column='title', max_length=100, blank=True)
    collection = models.ForeignKey(Collection, related_name='collecitons_list', on_delete=models.CASCADE, null=True)
    #collection = models.CharField(max_length=256, choices=list(Collection.objects.values_list("title", "title")), null= True, blank=True)
    description = RichTextField(blank=True, null=True)
    price = models.IntegerField(db_column='price', blank=True, default=0)
    discount = models.IntegerField(db_column='discount', blank=True, default=0)
    old_price = models.IntegerField(db_column='old_price', blank=True)
    size = models.CharField(db_column='size', max_length=100, blank=True)
    size_count = models.IntegerField(db_column='size_count', blank=True, default=0)
    fabric = models.CharField(db_column='fabric', max_length=100, blank=True)
    fabric_composition = models.CharField(db_column='fabric_composition', max_length=100, blank=True)
    hits = models.BooleanField(default=False)
    novelty = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if not self.old_price:
            self.old_price = self.price + self.price*self.discount/100
        a = self.size.split('-')
        if len(a) > 1:
            self.size_count = (int(a[1].strip()) - int(a[0].strip()))/2
        else:
            self.size_count = 1
        super(Product, self).save(*args, **kwargs)
    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    

# ProductImage
class ProductImage(models.Model):
    color = ColorField(db_column='color', default='#FFFFFF')
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    product = models.ForeignKey(Product, related_name='colors', on_delete=models.CASCADE)
    class Meta:
        db_table = 'productimage'
        verbose_name = 'ProductImage'
        verbose_name_plural = 'ProductImage'



