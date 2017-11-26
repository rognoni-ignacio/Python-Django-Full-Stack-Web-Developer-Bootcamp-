from django.contrib import admin
from blog_app.models import Author, Comment, Post

# Register your models here.
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Post)