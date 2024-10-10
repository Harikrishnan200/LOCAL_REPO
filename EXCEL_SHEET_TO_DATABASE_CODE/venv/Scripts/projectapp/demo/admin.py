from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Person
# Register your models here.

@admin.register(Person)
class PersonAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'email','location')