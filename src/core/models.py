from django.db import models

# Create your models here.
class CelestialBody(models.Model):

    name = models.CharField(max_length=150)
    mass = models.CharField(max_length=150)
    radius = models.CharField(max_length=150)
    age = models.CharField(max_length=150)
    description = models.CharField(max_length=5000)
    image = models.CharField(max_length=2048)

    def __str__(self):
        return self.name