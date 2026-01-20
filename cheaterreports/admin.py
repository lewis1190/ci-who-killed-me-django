from django.contrib import admin

from cheaterreports.models import CheaterPost, Vote

# Register your models here.


@admin.register(CheaterPost)
class CheaterPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'suspect_username', 'game_name',
                    'author', 'created_on')
    search_fields = ('title', 'suspect_username',
                     'game_name', 'author__username')
    list_filter = ('created_on', 'suspected_hack_types')


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'vote_type', 'created_on')
    search_fields = ('user__username', 'post__title')
    list_filter = ('vote_type', 'created_on')
