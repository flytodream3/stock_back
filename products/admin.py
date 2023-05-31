from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Category, SubCategory, Measure, Product


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name', 'author', 'created_at', 'updated_at')
    search_fields = ['name']


@admin.register(SubCategory)
class SubCategoryAdmin(ImportExportModelAdmin):
    list_display = ('name', 'category', 'author', 'created_at', 'updated_at')
    search_fields = ['name']
    list_filter = ['category']


@admin.register(Measure)
class MeasureAdmin(ImportExportModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['name', 'as_key', 'p_num', 'category', 'quantity', 'measure', 'count', 'out_count', 'stockroom', 'is_active', 'in_use']
    list_filter = ['category', 'subcategory', 'measure', 'stockroom']
    search_fields = ['name', 'as_key', 'p_num']
