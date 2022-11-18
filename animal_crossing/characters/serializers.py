from rest_framework import serializers

from .models import Villager

class VillagerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Villager