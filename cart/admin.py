from django.contrib import admin

# Register your models here.
from cart.models import *

admin.site.register(CartProducts)
admin.site.register(CartServiceLst)
admin.site.register(CartSimple)
admin.site.register(ClinicCart)
class CartProductsInline(admin.TabularInline):
    model = CartProducts
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra
class CartAdmin(admin.ModelAdmin):
    list_display = ['transaction_id','cust', 'business','conver','total','items','note','status']
    inlines = [CartProductsInline]
admin.site.register(Cart, CartAdmin)
