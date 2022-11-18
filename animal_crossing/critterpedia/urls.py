from django.urls import path
from .views import BugsView

urlpatterns = [
    path('', BugsView.as_view(), name='bugs'),
]