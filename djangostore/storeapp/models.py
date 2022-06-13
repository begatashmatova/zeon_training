from django.db import models
from ckeditor.fields import RichTextField

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
    item = models.CharField(db_column='title', max_length=100, blank=True)
    collection = models.CharField(max_length=256, choices=list(Collection.objects.values_list("title", "title")), null= True)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    description = RichTextField(blank=True, null=True)
    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title


