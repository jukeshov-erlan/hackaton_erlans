from rest_framework import serializers
from .models import *

class AutoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Auto
        fields = '__all__'


# class HouseSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     class Meta:
#         model = House
#         fields = ('estate', 'floor', 'location', 'price', 'body', 'user')