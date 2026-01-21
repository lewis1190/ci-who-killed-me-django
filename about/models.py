from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class About(models.Model):
    """
    Stores an About entry
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="about_posts"
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    about_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
