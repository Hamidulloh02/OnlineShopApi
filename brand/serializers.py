from rest_framework import serializers
from .models import Brand,Brandimages


class BrandImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brandimages
        fields = (
            'id', 'post', 'image'
        )

class  BrandSerializers(serializers.ModelSerializer):
    brandimages = BrandImagesSerializer(many=True)
    class Meta:
        model = Brand
        fields = ('id','brandname','brandlogo','saytlink','brandimages')
