from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Reservation, EmailConfirmation
from .serializers import ReservationSerializer, EmailConfirmationSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hotel', 'room', 'check_in_date', 'check_out_date', 'is_confirmed']


class EmailConfirmationViewSet(viewsets.ModelViewSet):
    queryset = EmailConfirmation.objects.all()
    serializer_class = EmailConfirmationSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['reservation', 'sent_at']
