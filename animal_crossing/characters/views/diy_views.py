from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.diy import Diy
from ..serializers import DiySerializer, DiyReadSerializer

# Create your views here.
# localhost:3000/hospital/diys/ get post
class DiysView(APIView):
    """View class for diys/ for viewing all and creating"""
    serializer_class = DiySerializer
    def get(self, request):
        diys = Diy.objects.all()
        serializer = DiyReadSerializer(diys, many=True)
        return Response({'diys': serializer.data})

    def post(self, request):
        serializer = DiySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# localhost:3000/hospital/diys/:id get delete update
class DiyDetailView(APIView):
    """View class for diys/:pk for viewing a single diy, updating a single diy, or removing a simgle diy"""
    serializer_class = DiySerializer
    def get(self, request, pk):
        diy = get_object_or_404(Diy, pk=pk)
        serializer = DiyReadSerializer(diy)
        return Response({'diy': serializer.data})

    def put(self, request, pk):
        diy = get_object_or_404(Diy, pk=pk)
        serializer = DiySerializer(diy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        diy = get_object_or_404(Diy, pk=pk)
        diy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)