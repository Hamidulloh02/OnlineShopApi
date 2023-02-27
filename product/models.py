from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    poster = models.ImageField(upload_to='images/',blank=True,verbose_name="Upload category image")
    name = models.CharField(max_length=100,verbose_name="Write category name")

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=100,verbose_name='Product name')
    price = models.IntegerField(verbose_name="Product price")
    statename = models.CharField(max_length=100,verbose_name="Product state name")
    factoryname = models.CharField(max_length=100,verbose_name="Product factory name")
    size = models.CharField(max_length=100,verbose_name="Product size")
    material = models.CharField(max_length=100,verbose_name="Product material")
    info = RichTextField(verbose_name="Product about info")
    posterdekor = models.ImageField(upload_to='images/',blank=True,verbose_name='Products dekor upload image')
    posterpol = models.ImageField(upload_to='images/',blank=True,verbose_name="Product pol upload image")
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True,verbose_name="Category")
    def __str__(self):
        return self.name

class Image(models.Model):
    post = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, related_name='posterinfo')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
       return f'Images of {self.post.id}'

