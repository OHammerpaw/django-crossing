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
