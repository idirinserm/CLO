from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Service
from .serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name', 'price']
    filterset_fields = ['name', 'price']
