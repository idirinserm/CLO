from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReservationViewSet, EmailConfirmationViewSet

router = DefaultRouter()
router.register(r'reservations', ReservationViewSet)
router.register(r'email-confirmations', EmailConfirmationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
