from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.villager import Villager
from ..serializers import VillagerSerializer

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

# localhost:3000/villagers/:id get delete update
class VillagerDetailView(APIView):
    """View class for villagers/:pk for viewing a single villager, updating a single villager, or removing a single villager"""
    def get(self, request, pk):
        villager = get_object_or_404(Villager, pk=pk)
        serializer = VillagerSerializer(villager)
        return Response({'villager': serializer.data})

    def patch(self, request, pk):
        villager = get_object_or_404(Villager, pk=pk)
        serializer = VillagerSerializer(villager, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        villager = get_object_or_404(Villager, pk=pk)
        villager.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)