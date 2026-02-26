"""Cross-cutting middleware.

This module contains small, dependency-free middleware components.

Why a custom security headers middleware?
- Django's SecurityMiddleware covers a good baseline.
- Some security headers (CSP, Permissions-Policy, Referrer-Policy) are
  application-specific and frequently tuned per project.

This middleware is intentionally conservative by default (report-only optional)
so it can be safely enabled progressively.
"""

from __future__ import annotations

from django.conf import settings

from .request_id import new_request_id, set_request_id


class SecurityHeadersMiddleware:
    """Add extra security headers.

    Controlled via settings:
    - SECURITY_HEADERS_ENABLED (bool)
    - CSP_ENABLED (bool)
    - CSP_REPORT_ONLY (bool)
    - CSP_POLICY (str)

    Notes
    -----
    - Start with CSP_REPORT_ONLY=True in production, inspect reports, then
      switch to enforcement.
    - Keep policies as a single string for simplicity.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if not getattr(settings, "SECURITY_HEADERS_ENABLED", True):
            return response

        # Referrer policy (privacy)
        response.headers.setdefault("Referrer-Policy", getattr(settings, "REFERRER_POLICY", "strict-origin-when-cross-origin"))

        # Permissions policy (reduce attack surface)
        response.headers.setdefault("Permissions-Policy", getattr(settings, "PERMISSIONS_POLICY", "geolocation=(), microphone=(), camera=()"))

        # Explicitly disable MIME sniffing
        response.headers.setdefault("X-Content-Type-Options", "nosniff")

        # CSP (optional)
        if getattr(settings, "CSP_ENABLED", False):
            header_name = "Content-Security-Policy-Report-Only" if getattr(settings, "CSP_REPORT_ONLY", True) else "Content-Security-Policy"
            policy = getattr(settings, "CSP_POLICY", "default-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'")
            response.headers.setdefault(header_name, policy)

        return response


class RequestIdMiddleware:
    """Ensure each request has a request id for correlation.

    - If client sends X-Request-ID, we keep it.
    - Otherwise we generate one.
    - We always return it in the response header.
    """

    header_name = "X-Request-ID"

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        rid = request.headers.get(self.header_name) or new_request_id()
        set_request_id(rid)
        response = self.get_response(request)
        response.headers.setdefault(self.header_name, rid)
        return response
