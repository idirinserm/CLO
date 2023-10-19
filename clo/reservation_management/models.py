from django.db import models

from hotel_management.models import Room
from service_management.models import Service


class Reservation(models.Model):
    hotel = models.ForeignKey('hotel_management.Hotel', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_confirmed = models.BooleanField(default=False)
    additional_services = models.ManyToManyField(Service)

    def __str__(self):
        return f"Reservation for {self.room} at {self.hotel}"


class EmailConfirmation(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    sent_at = models.DateTimeField()

    def __str__(self):
        return f"Confirmation for {self.reservation}"
