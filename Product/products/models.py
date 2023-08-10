from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=10)


    def __str__ (self):
        return self.name


class Favorite(models.Model):
    user_id= models.IntegerField()
    product= models.IntegerField()

    # product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Make sure it's not defined more than once
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user_id', 'product']

