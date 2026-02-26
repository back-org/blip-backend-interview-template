"""Utility API views (health checks, etc.)."""

from __future__ import annotations

from django.utils.timezone import now
import logging
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


logger = logging.getLogger(__name__)


class HealthCheckView(APIView):
    """Simple health check endpoint.

    Useful for load balancers / container orchestrators.
    """

    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"status": "ok", "timestamp": now().isoformat()})


class CSPReportView(APIView):
    """Receive CSP violation reports.

    Browsers send reports as JSON when you enable CSP report-only or report-uri.
    We keep this endpoint extremely lightweight: it only logs the payload.
    """

    permission_classes = [AllowAny]

    def post(self, request):
        payload = request.data
        # Avoid logging huge bodies; browsers typically send small JSON objects.
        logger.warning("CSP report received", extra={"csp_report": payload})
        return Response({"status": "ok"})
