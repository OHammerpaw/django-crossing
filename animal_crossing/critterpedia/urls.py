from django.urls import path
from .views import BugsView, BugDetailView

urlpatterns = [
    path('', BugsView.as_view(), name='bugs'),
    path('<int:pk>/', BugDetailView.as_view(), name='bug')
]