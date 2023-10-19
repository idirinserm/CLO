from django.db import models

from service_management.models import Service


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    base_rate = models.DecimalField(max_digits=10, decimal_places=2)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.name
