from django.db import models
from datetime import date
from django.utils import timezone
# Create your models here.

#User Model
class Users(models.Model):
    PK = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

#Product Models
class Products(models.Model):
    PK = models.BigIntegerField()
    SKU = models.IntegerField()
    product_type = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class ProductTaxonomyTerms(models.Model):
    PK = models.BigIntegerField()
    ptt_name = models.CharField(max_length=50)
    ptt_slug = models.SlugField(max_length=50)

class ProductTaxonomies(models.Model):
    PK = models.BigIntegerField()
    taxonomy_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

class ProductTerms(models.Model):
    PK = models.BigIntegerField()
    ptt_id = models.ForeignKey(ProductTaxonomyTerms, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)

#order models
class Orders(models.Model):
    PK = models.BigIntegerField()
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    customer_billing_address = models.CharField(max_length=255)
    customer_shipping_address = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    delivery_type = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
class OrderNotes(models.Model):
    PK = models.BigIntegerField()
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    order_description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
#Line Model
class LineItems(models.Model):
    PK = models.BigIntegerField()
    product_id = models.ForeignKey(ProductTaxonomyTerms, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    quality = models.CharField(max_length=255)
    price_incl_vat = models.IntegerField()
    price_excl_vat = models.IntegerField()

#Notifications Model
class Notifications(models.Model):
    PK = models.BigIntegerField()
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    push_id = models.IntegerField()
    notification_subject = models.CharField(max_length=255)
    notification_body = models.CharField(max_length=255)

#Pages
class Pages(models.Model):
    PK = models.BigIntegerField()
    title = models.CharField(max_length=50)
    featured_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    excerpt = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50)
    meta_description = models.CharField(max_length=150)

#Settings
class Settings(models.Model):
    PK = models.BigIntegerField()
    settings_name = models.CharField(max_length=50)
    settings_value = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

#Roles
class Roles(models.Model):
    PK = models.BigIntegerField()
    role_name = models.CharField(max_length=50)
    role_capabilities = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)