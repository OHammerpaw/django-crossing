from django.urls import path
from .views.villager_views import VillagersView, VillagerDetailView
from .views.diy_views import DiysView, DiyDetailView

urlpatterns = [
    path('villagers/', VillagersView.as_view(), name='villagers'),
    path('villagers/<int:pk>/', VillagerDetailView.as_view(), name='villager'),
    path('diys/', DiysView.as_view(), name='diy'),
    path('diys/<int:pk>/', DiyDetailView.as_view(), name='diy')
]