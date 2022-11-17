from django.db import models

# Create your models here.
class Villager(models.Model):
    name = models.CharField(max_length=15)
    personality = models.CharField(max_length=10)
    species = models.CharField(max_length=12)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} is a {self.personality} {self.species}"