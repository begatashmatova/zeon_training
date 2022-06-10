from django.db import models

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