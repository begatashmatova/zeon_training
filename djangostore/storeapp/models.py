from django.db import models
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Benefit(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000,
                                   blank=False)
    icon = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'benefit'
        verbose_name = 'Benefit'
        verbose_name_plural = 'Наши преимущества'

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
        verbose_name = 'Публичная оферта'
        verbose_name_plural = 'Публичная оферта'

    def __str__(self):
        return self.title


class MainPage(models.Model):
    link = models.CharField(db_column='link', max_length=100, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'mainpage'
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


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
        if not self.price:
            self.price = self.old_price*(1 - self.discount/100)
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

    def __str__(self):
        return str(self.color)

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
        choices=[
            ('Telegram', 'Telegram'),
            ('Whatsapp', 'Whatsapp'),
            ('Instagram', 'Instagram'),
            ('Mail', 'Mail'),
            ('Phone', 'Phone')
        ],
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
        if self.network_type == 'Mail':
            self.contact = 'mailto:' + self.contact
        if self.network_type == 'Phone':
            self.contact = 'callto:' + self.contact
        super(ContactInfo, self).save(*args, **kwargs)

    class Meta:
        db_table = 'contactinfo'
        verbose_name = 'ContactInfo'
        verbose_name_plural = 'ContactInfo'

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.cartitems.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.cartitems.all()
        total = sum([item.quantity for item in orderitems])
        return total 

    @property
    def get_products_count(self):
        orderitems = self.cartitems.all()
        total = sum([item.products_count for item in orderitems])
        return total 

    @property
    def get_discount_amount(self):
        orderitems = self.cartitems.all()
        total = sum([item.get_discount for item in orderitems])
        return total

    @property
    def get_final_price(self):
        orderitems = self.cartitems.all()
        total = sum([item.final_price for item in orderitems])
        return total

    @property
    def item_list(self):
        orderitems = self.cartitems.all()
        return orderitems


class Order(models.Model):
    cart = models.ForeignKey(
        Cart,
        related_name='carts',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    date_ordered = models.DateTimeField(auto_now_add=True)
    old_price = models.IntegerField(db_column='old_price', blank=True, default=0)
    discount = models.IntegerField(db_column='discount', blank=True, default=0)
    final_price = models.IntegerField(db_column='final_price', blank=True, default=0)
    products_count = models.IntegerField(db_column='products_count', blank=True, default=0)
    items_count = models.IntegerField(db_column='items_count', blank=True, default=0)

    def save(self, *args, **kwargs):
        if self.cart is not None:
            self.old_price = self.cart.get_cart_total
        else:
            orderitems = self.orderitems.all()
            self.old_price = sum([item.get_total for item in orderitems])

        if self.cart is not None:
            self.final_price = self.cart.get_final_price
        else:
            orderitems = self.orderitems.all()
            self.final_price = sum([item.final_price for item in orderitems])
        
        if self.cart is not None:
            self.products_count = self.cart.get_products_count
        else:
            orderitems = self.orderitems.all()
            self.products_count = sum([item.products_count for item in orderitems])

        if self.cart is not None:
            self.items_count = self.cart.get_cart_items
        else:
            orderitems = self.orderitems.all()
            self.items_count = sum([item.quantity for item in orderitems])

        if self.cart is not None:
            self.discount = self.cart.get_discount_amount
        else:
            orderitems = self.orderitems.all()
            self.discount = sum([item.get_discount for item in orderitems])

        super(Order, self).save(*args, **kwargs)      

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    cart = models.ForeignKey(
        Cart,
        related_name='cartitems',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    order = models.ForeignKey(
        Order,
        related_name='orderitems',
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    quantity = models.IntegerField(default=0, null=True, blank=True)
    color = models.ForeignKey(ProductImage, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    size = models.CharField(db_column='size', max_length=100, blank=True)
    price = models.IntegerField(db_column='final_price', blank=True, default=0)
    old_price = models.IntegerField(db_column='old_price', blank=True, default=0)

    def save(self, *args, **kwargs):
        self.size = self.product.size
        self.price = self.product.price
        self.old_price = self.product.old_price

        super(CartItem, self).save(*args, **kwargs) 

    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        total = self.product.old_price * self.quantity * self.product.size_count
        return total

    @property
    def get_discount(self):
        total = self.product.old_price * self.quantity * self.product.size_count - self.product.price * self.quantity * self.product.size_count
        return total

    @property
    def final_price(self):
        total = self.product.price * self.quantity * self.product.size_count
        return total

    @property
    def products_count(self):
        return self.product.size_count * self.quantity


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone_number = PhoneNumberField(null=True, blank=False)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    # date_created = models.DateTimeField(db_column='date_created', auto_now_add=True)

    date_created = models.DateTimeField(
        db_column='date_created',
        blank=True,
        null=True,
        default=datetime.now()
    )

    order_status = models.CharField(
        max_length=256,
        choices=[('New', 'Новый'), ('Completed', 'Оформлен'), ('Canceled', 'Отменен')],
        null=True,
        default='Новый'
    )

    def __str__(self):
        return self.address







