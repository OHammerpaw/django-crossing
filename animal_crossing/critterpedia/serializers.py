from rest_framework import serializers

from .models import Bug

class BugSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Bug
