from django.contrib import admin
from .models import User, Product, ProductTaxonomyTerm, ProductTaxonomie, ProductTerm, Order, OrderNote, LineItem, Notification, Page, Setting, Role, Category
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

# Register your models here.
admin.site.register (Product)
admin.site.register (ProductTaxonomyTerm)
admin.site.register (ProductTaxonomie)
admin.site.register (ProductTerm)
admin.site.register (Order)
admin.site.register (OrderNote)
admin.site.register (LineItem)
admin.site.register (Page)
admin.site.register (Setting)
admin.site.register (Role)
admin.site.register (Category)

#Class Forms

class UserForm(forms.ModelForm):
    class Meta:
        widgets = {
            'phone': PhoneNumberPrefixWidget()
        }

class NotificationForm(forms.ModelForm):
    class Meta:
        widgets = {
            'phone': PhoneNumberPrefixWidget() 
        }

#Custom Model registrations
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    form = NotificationForm