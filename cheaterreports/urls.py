from . import views
from django.urls import path

urlpatterns = [
    # path('', views.top_reports, name='top_reports'),
    # path('', views.reports_by_username, name='reports_by_username'),
    path('', views.new_report, name='new_report'),
    path('<int:report_id>/', views.report_detail, name='report_detail'),
]
