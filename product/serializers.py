from rest_framework import serializers

from product.models import Products,Category,Image


class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id', 'post', 'image'
        )
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','poster','name')

class ProductSerializer(serializers.ModelSerializer):
    posterinfo = PostImagesSerializer(many=True)
    category = CategorySerializers()
    class Meta:
        model = Products
        fields = ('id','name','price','statename','factoryname','size','material','info','posterdekor','posterpol','posterinfo','category','created_at')



