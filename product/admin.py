from django.contrib import admin
from .models import Products,Category,Image
# Register your models here.

class PostImagesInline(admin.TabularInline):
    model = Image
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [PostImagesInline]
    readonly_fields = ('updated_at', 'created_at')

admin.site.register(Products, PostAdmin)
admin.site.register(Category)
admin.site.register(Image)
