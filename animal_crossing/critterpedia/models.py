from django.db import models

# Create your models here.
class Bug(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    sell_price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} and can be found {self.location} and is worth {self.sell_price} bells."