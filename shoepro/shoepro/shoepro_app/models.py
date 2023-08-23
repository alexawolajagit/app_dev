from django.db import models
from datetime import date
from django.utils import timezone
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

#Roles
class Role(models.Model):
    role_name = models.CharField(max_length=50)
    role_capabilities = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

#User Model
class User(models.Model):
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = PhoneNumberField()
    role_id = models.ForeignKey(Role, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

#Brand model
class Brand(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)

#automatic slugify on save

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

#Gender Model

class Gender(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)

#automatic slugify on save

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

#Product Models
class Product(models.Model):
    SKU = models.IntegerField()
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class ProductTaxonomie(models.Model):
    taxonomy_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)

#automatic slugify on save

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.taxonomy_name)
        return super().save(*args, **kwargs)
    
class ProductTaxonomyTerm(models.Model):
    ptt_name = models.ForeignKey(ProductTaxonomie, on_delete=models.CASCADE)
    ptt_slug = models.SlugField(max_length=50, null=True, blank=True)

    #automatic slugify on save

    def save(self, *args, **kwargs):  
        if not self.ptt_slug:
            self.ptt_slug = slugify(self.ptt_name)
        return super().save(*args, **kwargs)

class ProductTerm(models.Model):
    ptt_id = models.ForeignKey(ProductTaxonomyTerm, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

#category model

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)

    #automatic slugify on save

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class CategoryProduct(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

#order models
class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    customer_billing_address = models.CharField(max_length=255)
    customer_shipping_address = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    delivery_type = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
class OrderNote(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
#Line Model
class LineItem(models.Model):
    product_id = models.ForeignKey(ProductTaxonomyTerm, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_incl_vat = models.DecimalField(max_digits=10, decimal_places=2)
    price_excl_vat = models.DecimalField(max_digits=10, decimal_places=2)

#Notifications Model
class Notification(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField()
    push_id = models.IntegerField()
    notification_subject = models.CharField(max_length=255)
    notification_body = models.CharField(max_length=255)

#Pages
class Page(models.Model):
    title = models.CharField(max_length=50)
    featured_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    excerpt = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50)
    meta_description = models.CharField(max_length=150)

    #automatic slugify on save

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

#Settings
class Setting(models.Model):
    settings_name = models.CharField(max_length=50)
    settings_value = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
