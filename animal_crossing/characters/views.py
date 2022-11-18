from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Villager
from .serializers import VillagerSerializer

# Create your views here.
class VillagersView(APIView):
    """View class for villagers/ for viewinmg all and creating"""
    def get(self, request):
        villagers = Villager.objects.all()
        serializer =VillagerSerializer(villagers, many=True)
        return Response({'villagers': serializer.data})

    def post(self, request):
        serializer = VillagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)