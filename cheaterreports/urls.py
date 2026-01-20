from . import views
from django.urls import path

urlpatterns = [
    #   Reports
    path('', views.list_reports, name='list_reports'),
    path('new/', views.new_report, name='new_report'),
    path('<int:report_id>/', views.report_detail, name='report_detail'),
    path('<int:report_id>/edit', views.report_edit, name='edit_report'),
    path('<int:report_id>/delete', views.report_delete, name='delete_report'),
    path('<int:report_id>/vote/<str:vote_type>/', views.vote_report,
         name='vote_report'),

    #  Comments
    path('<int:report_id>/comments/new/',
         views.add_comment, name='add_comment'),
    path('comments/<int:comment_id>/edit',
         views.edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete',
         views.delete_comment, name='delete_comment'),

]
