from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import NewsPost

# Register your models here.


@admin.register(NewsPost)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    summernote_fields = ('content',)
