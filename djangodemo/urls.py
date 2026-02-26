from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
# from .views import home
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

urlpatterns = [
                  path("", include("django_prometheus.urls")),

                  # Auth (JWT)
                  path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
                  path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
                  path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
                  path("api/token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),

                  path("schema/", include("apps.spectacular.urls")),
                  path("users/", include("apps.users.urls")),
                  path("", include("apps.utils.urls")),

                  path("", include("apps.pages.urls")),
                  path("admin/", admin.site.urls),
                  re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon-v5.png')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if getattr(settings, "SILK_ENABLED", False):
    urlpatterns = [path("silk/", include("silk.urls", namespace="silk"))] + urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
