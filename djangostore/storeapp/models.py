from django.db import models
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField


class Benefit(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000,
                                   blank=False)
    icon = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'benefit'
        verbose_name = 'Benefit'
        verbose_name_plural = 'Benefits'

    def __str__(self):
        return self.title


class Collection(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'collection'
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = RichTextField(blank=True, null=True)
    photo1 = models.ImageField(null=True, blank=True, upload_to='images/')
    photo2 = models.ImageField(null=True, blank=True, upload_to='images/')
    photo3 = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = RichTextField(blank=True, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'news'
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class PublicOffer(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = RichTextField(blank=True, null=True)

    class Meta:
        db_table = 'publicoffer'
        verbose_name = 'Publicoffer'
        verbose_name_plural = 'Public offers'

    def __str__(self):
        return self.title


class MainPage(models.Model):
    link = models.CharField(db_column='link', max_length=100, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'mainpage'
        verbose_name = 'Main page'
        verbose_name_plural = 'Main pages'

    def __str__(self):
        return self.title


class Product(models.Model):
    item = models.CharField(db_column='item', max_length=100, blank=True)
    title = models.CharField(db_column='title', max_length=100, blank=True)
    collection = models.ForeignKey(
        Collection,
        related_name='collecitons_list',
        on_delete=models.CASCADE,
        null=True
    )
    description = RichTextField(blank=True, null=True)
    price = models.IntegerField(db_column='price', blank=True, default=0)
    discount = models.IntegerField(
        db_column='discount',
        blank=True,
        default=0
    )
    old_price = models.IntegerField(db_column='old_price', blank=True)
    size = models.CharField(db_column='size', max_length=100, blank=True)
    size_count = models.IntegerField(
        db_column='size_count',
        blank=True,
        default=0
    )
    fabric = models.CharField(db_column='fabric', max_length=100, blank=True)
    fabric_composition = models.CharField(
        db_column='fabric_composition',
        max_length=100,
        blank=True
    )
    hits = models.BooleanField(default=False)
    novelty = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.old_price:
            self.old_price = self.price + self.price*self.discount/100
        a = self.size.split('-')
        if len(a) > 1:
            self.size_count = (int(a[1].strip()) - int(a[0].strip()))/2 + 1
        else:
            self.size_count = 1
        super(Product, self).save(*args, **kwargs)

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    color = ColorField(db_column='color', default='#FFFFFF')
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    product = models.ForeignKey(
        Product,
        related_name='colors',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'productimage'
        verbose_name = 'ProductImage'
        verbose_name_plural = 'ProductImage'


class Help(models.Model):
    question = models.CharField(
        db_column='quesion',
        max_length=100,
        blank=True
    )
    answer = models.CharField(
        db_column='answer',
        max_length=100,
        blank=True
    )

    class Meta:
        db_table = 'help'
        verbose_name = 'Help'
        verbose_name_plural = 'Help'


class HelpImage(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'helpimage'
        verbose_name = 'HelpImage'
        verbose_name_plural = 'HelpImage'


class Call(models.Model):
    name = models.CharField(
        db_column='name',
        max_length=100,
        blank=True
    )
    number = models.CharField(
        db_column='number',
        max_length=100,
        blank=True
    )
    call_type = models.CharField(
        db_column='call_type',
        max_length=100,
        blank=True
    )
    call_date = models.DateTimeField(
        db_column='call_date',
        blank=True,
        null=True
    )
    call_status = models.CharField(
        max_length=256,
        choices=[('Yes', 'Yes'), ('No', 'No')],
        null=True,
        default='No'
    )

    def save(self, *args, **kwargs):
        self.call_date = datetime.now()
        self.call_type = 'Back call'
        super(Call, self).save(*args, **kwargs)

    class Meta:
        db_table = 'call'
        verbose_name = 'Call'
        verbose_name_plural = 'Calls'


class Footer(models.Model):
    description = models.CharField(db_column='description', max_length=100, blank=False)
    header_logo = models.ImageField(null=True, blank=True, upload_to='images/')
    footer_logo = models.ImageField(null=True, blank=True, upload_to='images/')
    header_number = PhoneNumberField(null=False, blank=False, unique=True)

    class Meta:
        db_table = 'footer'
        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'


class ContactInfo(models.Model):
    network_type = models.CharField(
        max_length=256,
        choices=[('Telegram', 'Telegram'), ('Whatsapp', 'Whatsapp'), ('Instagram', 'Instagram')],
        null=True
    )
    contact = models.CharField(db_column='contact', max_length=100, blank=False)
    footer = models.ForeignKey(
        Footer,
        related_name='contacts',
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        if self.network_type == 'Telegram':
            self.contact = 'https://t.me/' + self.contact
        if self.network_type == 'Whatsapp':
            self.contact = 'https://wa.me/' + self.contact
        if self.network_type == 'Instagram':
            self.contact = 'https://www.instagram.com/' + self.contact
        super(ContactInfo, self).save(*args, **kwargs)

    class Meta:
        db_table = 'contactinfo'
        verbose_name = 'ContactInfo'
        verbose_name_plural = 'ContactInfo'
