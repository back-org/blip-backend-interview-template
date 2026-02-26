from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
# from .views import home
from django.views.generic import RedirectView

urlpatterns = [
                  path("schema/", include("apps.spectacular.urls")),
                  path("users/", include("apps.users.urls")),
                  path("", include("apps.utils.urls")),

                  path("", include("apps.pages.urls")),
                  path("admin/", admin.site.urls),
                  re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon-v5.png')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
