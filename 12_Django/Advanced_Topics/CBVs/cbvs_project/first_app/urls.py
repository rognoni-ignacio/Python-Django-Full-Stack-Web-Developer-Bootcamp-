from django.conf.urls import url
from first_app import views

app_name = 'first_app'

urlpatterns = [
    url(r'^$', views.SchoolListView.as_view(), name='school-list'),
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='school-detail'),
    url(r'^create/$', views.SchoolCreateView.as_view(), name='school-create'),
    url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='school-update'),
    url(r'^delete/ (?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='school-delete'),
]
