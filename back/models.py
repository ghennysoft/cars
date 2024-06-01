from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from shortuuid.django_fields import ShortUUIDField
from  django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='category/')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'SubCategories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    prod_id=ShortUUIDField(unique=True, length=35, max_length=50, prefix='prod_', alphabet='abcdefghijk1234567890')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, related_name='subcategory')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='brand')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product/', default='/images/default-image.png')
    description = RichTextUploadingField()
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=0)
    old_price = models.PositiveIntegerField(default=0)
    payed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name+' -- by -- '+self.subcategory.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id


class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id=ShortUUIDField(unique=True, length=30, max_length=50, prefix='prod_', alphabet='abcdefghijk1234567890')
    total = models.FloatField(default=0)
    payed = models.BooleanField(default=False) 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    adresse = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Commande n°{self.id}'


class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    cart_id=ShortUUIDField(unique=True, length=20, max_length=30, prefix='prod_', alphabet='abcdefghijk1234567890')
    invoice_no = models.CharField(max_length=150)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=0)
    total = models.FloatField(default=0)
    payed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.invoice_no)
