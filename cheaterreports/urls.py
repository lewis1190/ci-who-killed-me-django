from . import views
from django.urls import path

urlpatterns = [
    # path('', views.top_reports, name='top_reports'),
    # path('', views.reports_by_username, name='reports_by_username'),
    path('', views.list_reports, name='list_reports'),
    path('new/', views.new_report, name='new_report'),
    path('<int:report_id>/', views.report_detail, name='report_detail'),
    path('<int:report_id>/edit', views.report_edit, name='edit_report'),
    path('<int:report_id>/delete', views.report_delete, name='delete_report'),
    path('<int:report_id>/vote/<str:vote_type>/', views.vote_report,
         name='vote_report'),
]
