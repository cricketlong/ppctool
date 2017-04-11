from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^full_table$', views.full_table, name='full_table'),
    url(r'^([\d]+)[/]?$', views.campaign, name='campaign'),
    url(r'^([\d]+)/([\d]+)[/]?$', views.adgroup, name='adgroup'),
    url(r'^([\d]+)/([\d]+)/([\d]+)[/]?$', views.keyword, name='keyword')
]
