from django.conf.urls import url
from first_app import views

app_name = 'first_app'

urlpatterns = [
    url(r'^$', views.SchoolListView.as_view(), name='school-list'),
    url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='school-detail')
]
