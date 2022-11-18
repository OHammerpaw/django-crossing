from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Bug
from .serializers import BugSerializer

# Create your views here.
class BugsView(APIView):
    """View class for bugs/ for viewinmg all and creating"""
    def get(self, request):
        bugs = Bug.objects.all()
        serializer =BugSerializer(bugs, many=True)
        return Response({'bugs': serializer.data})

    def post(self, request):
        serializer = BugSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# localhost:3000/bugs/:id get delete update
class BugDetailView(APIView):
    """View class for bugs/:pk for viewing a single bug, updating a single bug, or removing a single bug"""
    def get(self, request, pk):
        bug = get_object_or_404(Bug, pk=pk)
        serializer = BugSerializer(bug)
        return Response({'bug': serializer.data})

    def patch(self, request, pk):
        bug = get_object_or_404(Bug, pk=pk)
        serializer = BugSerializer(bug, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bug = get_object_or_404(Bug, pk=pk)
        bug.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)