from django.db import models
from ckeditor.fields import RichTextField

# Benefits
class Benefit(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    icon = models.BinaryField(db_column='icon', blank=True, null=True, editable=True)
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
    photo = models.BinaryField(db_column='photo', blank=True, null=True, editable=True)
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
    photo1 = models.BinaryField(db_column='photo1', blank=True, null=True, editable=True)
    photo2 = models.BinaryField(db_column='photo2', blank=True, null=True, editable=True)
    photo3 = models.BinaryField(db_column='photo3', blank=True, null=True, editable=True)
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
    photo = models.BinaryField(db_column='photo', blank=True, null=True, editable=True)
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
        verbose_name_plural = 'Publicoffers'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title



# Main Page
class MainPage(models.Model):
    link = models.CharField(db_column='link', max_length=100, blank=True)
    photo = models.BinaryField(db_column='photo', blank=True, null=True, editable=True)
    class Meta:
        db_table = 'mainpage'
        verbose_name = 'Main page'
        verbose_name_plural = 'Main pages'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title