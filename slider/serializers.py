from rest_framework import serializers

from slider.models import Slider,Position
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id','name')


class SliderSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    class Meta:
        model = Slider
        fields = ('position','text','poster')
