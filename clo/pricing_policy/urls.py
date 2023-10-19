from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PricePolicyViewSet

router = DefaultRouter()
router.register(r'price-policies', PricePolicyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
