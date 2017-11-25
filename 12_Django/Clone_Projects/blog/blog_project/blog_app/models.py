from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User)
    personal_site = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile-pictures', blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    name = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, related_name='authors')

    def __str__(self):
        return self.name
