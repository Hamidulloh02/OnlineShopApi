from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Slider(models.Model):
    position =  models.ForeignKey(Position,on_delete=models.SET_NULL, null=True,verbose_name="Position")
    text = RichTextField()
    poster = models.ImageField(upload_to='images/', blank=True,verbose_name="Upload images")

    def __str__(self):
        return self.text

