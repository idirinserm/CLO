from django.contrib import admin
from reservation_management.models import Reservation, EmailConfirmation


class EmailConfirmationAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'sent_at')
    search_fields = ('reservation', 'sent_at')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'room', 'check_in_date', 'check_out_date', 'is_confirmed')
    search_fields = ('hotel__name', 'room__name', 'check_in_date', 'check_out_date')


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(EmailConfirmation, EmailConfirmationAdmin)
