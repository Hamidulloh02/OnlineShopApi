from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Brand(models.Model):
    brandname = models.CharField(max_length=100,verbose_name='Brand name')
    brandlogo = models.ImageField(upload_to='images/',blank=True)
    saytlink = models.URLField(("Sayt link"), max_length=128, db_index=True, unique=True, blank=True)
    brandinfo = RichTextField()

    def __str__(self):
        return self.brandname



class Brandimages(models.Model):
    post = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='brandimages')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
       return f'Brandimages of {self.post.id}'
