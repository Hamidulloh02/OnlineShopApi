from django.contrib import admin
from .models import Brand,Brandimages
# Register your models here.

class BrandImagesInline(admin.TabularInline):
    model = Brandimages
    extra = 0

class BrandAdmin(admin.ModelAdmin):
    inlines = [BrandImagesInline]
    readonly_fields = ()

admin.site.register(Brand, BrandAdmin)