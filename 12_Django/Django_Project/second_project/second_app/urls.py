from django.conf.urls import url
from second_app import views

urlpatterns = [
    url(r'^$', views.help, name='help'),
]