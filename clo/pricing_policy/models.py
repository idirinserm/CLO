from django.db import models
from hotel_management.models import Hotel


class PricePolicy(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)
    is_weekend = models.BooleanField()
    is_single_occupancy = models.BooleanField()
    price_adjustment = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Price Policy for {self.hotel} - {self.day_of_week}"
