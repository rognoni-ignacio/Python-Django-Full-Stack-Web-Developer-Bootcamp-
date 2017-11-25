from django.conf.urls import url
from blog_app import views

app_name = 'blog_app'

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='blog-index'),
]
