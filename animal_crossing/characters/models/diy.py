from django.db import models
from .villager import Villager

class Diy(models.Model):
    name = models.CharField(max_length=100)
    materials = models.CharField(max_length=100)
    buy_price = models.CharField(max_length=20)
    villager = models.ForeignKey(
        Villager,
        on_delete=models.CASCADE,
        related_name='gifted_diys'
    )

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} can be made using {self.materials}"