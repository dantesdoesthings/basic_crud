from django.db import models

# Create your models here.


class Gun(models.Model):
    name = models.CharField(max_length=50)
    propellant = models.CharField(max_length=50)
    calibre = models.CharField(max_length=10)
    manufacturer = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    magazine_capacity = models.IntegerField()
    first_manufactured = models.DateField(null=True)

