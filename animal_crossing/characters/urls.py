from django.urls import path
from .views import VillagersView, VillagerDetailView

urlpatterns = [
    path('', VillagersView.as_view(), name='villagers'),
    path('<int:pk>/', VillagerDetailView.as_view(), name='villager')
]