from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Hotel Reservation API",
        default_version='v1',
        description="API for managing hotels, reservations, services, and pricing policies",
        terms_of_service="https://www.etna-hotels.com/terms/",
        contact=openapi.Contact(email="contact@etna-hotels-alternance.net"),
        license=openapi.License(name="ETNA"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hotel-management/', include('hotel_management.urls')),
    path('api/service-management/', include('service_management.urls')),
    path('api/reservation-management/', include('reservation_management.urls')),
    path('api/pricing-policy/', include('pricing_policy.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
