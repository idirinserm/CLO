from django.contrib import admin
from .models import PricePolicy


@admin.register(PricePolicy)
class PricePolicyAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'day_of_week', 'is_weekend', 'is_single_occupancy', 'price_adjustment')
    search_fields = ('hotel__name', 'day_of_week')
