from django.contrib import admin
from .models import Contact, Featured ,CheckOut,Ethnic,Western,Party,Paksthani,Prayer,Product

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    
@admin.register(CheckOut)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')

admin.site.register(Featured)
admin.site.register(Prayer)
admin.site.register(Ethnic)
admin.site.register(Paksthani)
admin.site.register(Western)
admin.site.register(Party)
admin.site.register(Product)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'filter_class')

