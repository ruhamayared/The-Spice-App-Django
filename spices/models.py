from django.db import models

# Create your models here.
class Spice(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.CharField(max_length=300)