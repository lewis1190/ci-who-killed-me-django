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
    score = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']


class Vote(models.Model):
    VOTE_CHOICES = [
        ('up', 'Upvote'),
        ('down', 'Downvote'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='votes'
    )
    post = models.ForeignKey(
        CheaterPost, on_delete=models.CASCADE, related_name='votes'
    )
    vote_type = models.CharField(max_length=4, choices=VOTE_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
        indexes = [
            models.Index(fields=['user', 'post']),
        ]

    def __str__(self):
        vote_label = f"{self.user.username} voted {self.vote_type}"
        return f"{vote_label} on {self.post.title}"


class Comment(models.Model):
    """
    Stores a single comment related to :model:`cheaterreports.CheaterPost` and
     :model:`auth.User`.
    """
    post = models.ForeignKey(
        CheaterPost, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenter')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
