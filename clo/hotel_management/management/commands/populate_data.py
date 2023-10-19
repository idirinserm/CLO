from django.core.management.base import BaseCommand
from hotel_management.models import Hotel, Room
from service_management.models import Service
from reservation_management.models import Reservation, EmailConfirmation
from pricing_policy.models import PricePolicy
from schedule.models import Event, Calendar
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Populate the database with sample data according to customer requirements'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Populating the database with sample data...'))

        # Create sample hotels
        hotel1 = Hotel.objects.create(name='Hotel de Paris', address='123 Rue de la Paix, Paris',
                                      phone_number='+33 1 23 45 67 89')
        hotel2 = Hotel.objects.create(name='Château de Provence', address='789 Rue des Lavandes, Provence',
                                      phone_number='+33 4 56 71 23 45')

        room1 = Room.objects.create(name='Presidential Suite (SR)', capacity=5, base_rate=1000, hotel=hotel1)
        room2 = Room.objects.create(name='Suite (S)', capacity=3, base_rate=720, hotel=hotel1)
        room3 = Room.objects.create(name='Junior Suite (JS)', capacity=2, base_rate=500, hotel=hotel1)
        room4 = Room.objects.create(name='Deluxe Room (CD)', capacity=2, base_rate=300, hotel=hotel1)
        room5 = Room.objects.create(name='Standard Room (CS)', capacity=2, base_rate=150, hotel=hotel1)

        room6 = Room.objects.create(name='Presidential Suite (SR)', capacity=5, base_rate=1000, hotel=hotel2)
        room7 = Room.objects.create(name='Presidential Suite (SR)', capacity=5, base_rate=1000, hotel=hotel2)

        service1 = Service.objects.create(name='Parking space', price=25)
        service2 = Service.objects.create(name='Baby bed', price=0)
        service3 = Service.objects.create(name='Romance package', price=50)
        service4 = Service.objects.create(name='Breakfast', price=30)

        # Create reservations and calendar events
        def create_reservation_and_event(hotel, room, check_in_date, check_out_date, total_price, is_confirmed,
                                         services):
            reservation = Reservation.objects.create(hotel=hotel, room=room, check_in_date=check_in_date,
                                                     check_out_date=check_out_date, total_price=total_price,
                                                     is_confirmed=is_confirmed)
            reservation.additional_services.add(*services)
            EmailConfirmation.objects.create(reservation=reservation, sent_at=datetime.now())

            # Create an event in the calendar for the reservation
            calendar, created = Calendar.objects.get_or_create(name='Reservations')

            start_date = check_in_date
            end_date = check_out_date + timedelta(days=1)
            event = Event()
            event.calendar = calendar
            event.title = f"Reservation for {room} at {hotel}"
            event.start = start_date
            event.end = end_date
            event.reservation = reservation
            event.save()

        create_reservation_and_event(hotel1, room2, datetime(2023, 10, 20), datetime(2023, 10, 25), 3600,
                                     is_confirmed=True, services=[service1, service3, service4])

        create_reservation_and_event(hotel2, room6, datetime(2023, 10, 22), datetime(2023, 10, 24), 2000,
                                     is_confirmed=True, services=[service1, service2])

        PricePolicy.objects.create(hotel=hotel1, day_of_week='Friday', is_weekend=True, is_single_occupancy=False,
                                   price_adjustment=15)
        PricePolicy.objects.create(hotel=hotel1, day_of_week='Saturday', is_weekend=True, is_single_occupancy=False,
                                   price_adjustment=15)
        PricePolicy.objects.create(hotel=hotel1, day_of_week='Wednesday', is_weekend=False, is_single_occupancy=False,
                                   price_adjustment=-10)
        PricePolicy.objects.create(hotel=hotel1, day_of_week='Thursday', is_weekend=False, is_single_occupancy=False,
                                   price_adjustment=-10)
        PricePolicy.objects.create(hotel=hotel1, day_of_week='Monday', is_weekend=False, is_single_occupancy=False,
                                   price_adjustment=0)

        self.stdout.write(self.style.SUCCESS('Sample data populated successfully.'))
