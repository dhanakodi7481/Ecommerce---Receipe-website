from django.contrib import admin
from . models import Products,Customer,Cart, Order, Wishlist
from django.contrib.auth.models import Group
# Register your models here.
@admin.register(Products)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','state','zipcode']

@admin.register(Cart)
class CartModelAdmin (admin.ModelAdmin):
	list_display = ['id', 'user','product', 'quantity' ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'product')

admin.site.register(Order, OrderAdmin)

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added_on')

admin.site.unregister(Group)