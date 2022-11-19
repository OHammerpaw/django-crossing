from django.urls import path
from .views import BugsView, BugDetailView

urlpatterns = [
    path('bugs/', BugsView.as_view(), name='bugs'),
    path('bugs/<int:pk>/', BugDetailView.as_view(), name='bug')
]