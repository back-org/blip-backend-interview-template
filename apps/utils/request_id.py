"""Request ID utilities.

This module provides a tiny, dependency-free way to:

- Generate a request id per incoming request
- Expose it via a response header (X-Request-ID)
- Inject it into logs (via a logging Filter)

Why: in production, correlating a single request across logs and metrics is
critical for debugging and incident response.
"""

from __future__ import annotations

import contextvars
import uuid
from typing import Optional


_request_id: contextvars.ContextVar[Optional[str]] = contextvars.ContextVar(
    "request_id", default=None
)


def new_request_id() -> str:
    """Create a new opaque request id."""

    return uuid.uuid4().hex


def set_request_id(value: str) -> None:
    """Set request id for the current context."""

    _request_id.set(value)


def get_request_id() -> Optional[str]:
    """Return request id for the current context, if any."""

    return _request_id.get()


class RequestIdFilter:
    """Attach request_id to every log record."""

    def filter(self, record) -> bool:  # pragma: no cover
        record.request_id = get_request_id() or "-"
        return True
