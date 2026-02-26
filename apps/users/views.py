"""Users API.

Notes
-----
- Uses DRF viewsets for standard CRUD.
- Adds an extra admin-only endpoint (PermissionView) used in the template.
- Applies a stricter rate limit to user creation to reduce abuse.
"""

from __future__ import annotations

from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema, extend_schema_view

from .models import User
from .serializers import UserSerializer


@extend_schema_view(
    list=extend_schema(description="Return the list of users.", responses={200: UserSerializer}, methods=["get"]),
    create=extend_schema(description="Create a user.", request=UserSerializer, responses={201: UserSerializer}, methods=["post"]),
    retrieve=extend_schema(description="Retrieve a user by id.", responses={200: UserSerializer}, methods=["get"]),
    update=extend_schema(description="Update a user by id.", request=UserSerializer, responses={200: UserSerializer}, methods=["put"]),
    partial_update=extend_schema(description="Partially update a user by id.", request=UserSerializer, responses={200: UserSerializer}, methods=["patch"]),
    destroy=extend_schema(description="Delete a user by id.", responses={204: None}, methods=["delete"]),
)
class UserViewSet(viewsets.ModelViewSet):
    """CRUD operations for users."""

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by("id")

    @method_decorator(ratelimit(key="ip", rate="10/m", method="POST", block=True))
    def create(self, request, *args, **kwargs):
        """Create a user (rate-limited)."""
        return super().create(request, *args, **kwargs)


class PermissionView(APIView):
    """Example admin-only endpoint."""

    permission_classes = (IsAdminUser,)

    @extend_schema(request=None, description="User requests only for admin.")
    def get(self, request):
        serializer = UserSerializer(User.objects.all().order_by("id"), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
