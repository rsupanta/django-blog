from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(default='default.webp', upload_to='profile_pics')
    bio = models.TextField(max_length=256, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
