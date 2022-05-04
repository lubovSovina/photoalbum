from rest_framework import serializers
from .models import Photo
from ..user.serializers import UserSerializer


class PhotoSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Photo
        fields = '__all__'
