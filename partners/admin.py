from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Division


@admin.register(Division)
class DivisionAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', 'contact', 'phone']
    search_fields = ['code', 'name', 'contact', 'phone']
