from django.contrib import admin
from . import models

# Register your models here.

# NAME -> THE NAME OF THE MODEL + ADMIN
class MovieAdmin(admin.ModelAdmin):
    fields = ['title', 'release_year', 'length']


admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)