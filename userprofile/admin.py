from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import UserProfile

# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('user', 'created_on')
    search_fields = ('user__username',)
