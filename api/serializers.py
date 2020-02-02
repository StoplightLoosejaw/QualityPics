from .models import Pic
from rest_framework import serializers

class PicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pic
        fields = '__all__'
