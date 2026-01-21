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

    # Override to prepopulate author field with the logged-in admin on the
    # admin portal

    def get_changeform_initial_data(self, request):
        """
        Prepopulate the author field with the currently logged-in user
        when creating a new NewsPost.
        """
        initial_data = super().get_changeform_initial_data(request)
        if request.user.pk:
            initial_data['author'] = request.user.pk
        return initial_data
