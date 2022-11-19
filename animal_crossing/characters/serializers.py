from rest_framework import serializers

from .models.villager import Villager
from .models.diy import Diy


class DiySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Diy

class DiyReadSerializer(serializers.ModelSerializer):
    villager = serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = Diy

class VillagerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Villager
