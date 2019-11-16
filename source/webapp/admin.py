from django.contrib import admin

from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'description','image']
    exclude = []
    list_display_links = ['name']
    list_filter = ['category']

admin.site.register(Product, ProductAdmin)