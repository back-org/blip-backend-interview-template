from django.urls import path

from .apiviews import HealthCheckView

app_name = "utils"

urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health"),
]
