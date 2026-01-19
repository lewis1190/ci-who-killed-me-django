from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CheaterPost(models.Model):
    HACK_TYPE_CHOICES = [
        ('aimbot', 'Aimbot'),
        ('esp', 'ESP'),
        ('wallhack', 'Wallhack'),
        ('speedhack', 'Speed Hack'),
        ('noclip', 'No Clip'),
        ('other', 'Other'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    suspect_username = models.CharField(max_length=255)
    game_name = models.CharField(max_length=255)
    youtube_url = models.URLField()
    suspected_hack_types = models.JSONField(default=list)
    description = models.TextField()
    # score = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']
