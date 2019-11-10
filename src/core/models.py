from django.db import models

# Create your models here.
class CelestialBody(models.Model):

    BODY_TYPES = (
        ('S', 'Star'),
        ('M', 'Moon'),
        ('TP', 'Terrestrial Planets'),
        ('GG', 'Gas Giants'),
        ('IG', 'Ice Giants'),
        ('DP', 'Dwarf Planets'),
    )

    name = models.CharField(max_length=150)
    
    mass = models.FloatField()
    radius = models.FloatField()
    age = models.FloatField()
    
    body_type = models.CharField(max_length=2, choices=BODY_TYPES)
    description = models.CharField(max_length=5000)
    image = models.CharField(max_length=2048)


    def __str__(self):
        return self.name