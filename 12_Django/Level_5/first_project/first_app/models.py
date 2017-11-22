from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to='profile-pictures', blank=True)
    portfolio_site = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
