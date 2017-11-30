from django.conf.urls import url
from . import views

app_name = 'groups'

urlpatterns = [
    url(r"^$", views.ListGroup.as_view(), name='all'),
    url(r"^new/", views.CreateGroupView.as_view(), name='create'),
    url(r"post/in/(?P<slug>[-\w])/$", views.SingleGroup.as_view(), name='single'),
]