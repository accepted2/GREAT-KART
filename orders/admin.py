from django.contrib import admin
from .models import Payment,Order,OrderProduct
# Register your models here.

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment','user','product','quantity', 'product_price','ordered')
    extra = 0
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'order_total', 'tax', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered',]
    search_fields = ['order_number','first_name', 'last_name', 'email',]
    list_per_page =20
    inlines = [OrderProductInline]


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
admin.site.register(Order,OrderAdmin)
admin.site.register(Payment)
admin.site.register(OrderProduct)
