from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import StockRoom


@admin.register(StockRoom)
class StockRoomAdmin(ImportExportModelAdmin):
    list_display = ['name', 'author', 'created_at', 'updated_at']
    search_fields = ['name']
