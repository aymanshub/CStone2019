from django.contrib import admin
from .models import Stone, Category, Product, Processing


@admin.register(Stone)
class StoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Processing)
class ProcessingAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = [
        'category', 'stone', 'name', 'length', 'width',
        'processing', 'stock_units', 'available', 'price', 'image',
        'total_space_m',
    ]
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('category', 'stone',
                                    'name', 'length', 'width')}
