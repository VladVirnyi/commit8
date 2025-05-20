from django.contrib import admin
from .models import MenuCategory, MenuItem, Order


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_available', 'display_order']
    list_editable = ['is_available', 'display_order']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_available', 'temperature', 'size']
    list_filter = ['category', 'is_available', 'temperature', 'is_special']
    search_fields = ['name', 'description']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'product', 'order_date']
    list_filter = ['order_date']
    search_fields = ['customer_name', 'customer_phone', 'customer_email']

