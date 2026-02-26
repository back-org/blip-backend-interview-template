"""Utility API views (health checks, etc.)."""

from __future__ import annotations

from django.utils.timezone import now
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    """Simple health check endpoint.

    Useful for load balancers / container orchestrators.
    """

    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"status": "ok", "timestamp": now().isoformat()})
