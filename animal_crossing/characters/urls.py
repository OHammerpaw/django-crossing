from django.urls import path
from .views import VillagersView

urlpatterns = [
    path('', VillagersView.as_view(), name='villagers'),
]