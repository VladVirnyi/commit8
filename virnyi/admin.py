from django.contrib import admin
from .models import MenuCategory, MenuItem


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_available', 'display_order']
    list_editable = ['is_available', 'display_order']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_available', 'temperature', 'size']
    list_filter = ['category', 'is_available', 'temperature', 'is_special']
    search_fields = ['name', 'description']

