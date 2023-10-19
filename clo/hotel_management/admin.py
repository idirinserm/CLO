from django.contrib import admin
from .models import Hotel, Room


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number')
    search_fields = ('name', 'address', 'phone_number')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'base_rate', 'hotel')
    search_fields = ('name', 'hotel__name')
