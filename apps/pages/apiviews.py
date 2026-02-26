"""
API views for the pages application.

All views are read-only (GET only) and publicly accessible.
Uses DRF generic views for cleaner, more maintainable code.
"""

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import Address, Link, Menu, Service
from .serializers import AddressSerializer, LinkSerializer, MenuSerializer, ServiceSerializer


class MenuListAPIView(ListAPIView):
    """
    GET /api/menus/

    Returns the list of all active navigation menus,
    each including their nested child items.
    """

    serializer_class = MenuSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """Return only active menus, prefetching related items to avoid N+1 queries."""
        return Menu.objects.filter(is_active=True).prefetch_related("items")


class ServiceListAPIView(ListAPIView):
    """
    GET /api/services/

    Returns the list of all active services.
    """

    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Service.objects.filter(is_active=True)


class LinkListAPIView(ListAPIView):
    """
    GET /api/links/

    Returns the list of all active links.
    """

    serializer_class = LinkSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Link.objects.filter(is_active=True)


class AddressDetailAPIView(RetrieveAPIView):
    """
    GET /api/info/

    Returns the site's contact/address information.
    Uses the first Address record found (there should typically be only one).
    """

    serializer_class = AddressSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        """Retrieve the primary site address, or raise 404 if none exists."""
        return Address.objects.first()
