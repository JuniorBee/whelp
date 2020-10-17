from django.contrib import admin

# Register your models here.
from core.models import File, PDFContent


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass


@admin.register(PDFContent)
class PDFContentAdmin(admin.ModelAdmin):
    pass
