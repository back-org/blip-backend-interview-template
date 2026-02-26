from django.urls import path

from .apiviews import HealthCheckView, CSPReportView

app_name = "utils"

urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health"),
    path("csp-report/", CSPReportView.as_view(), name="csp_report"),
]
