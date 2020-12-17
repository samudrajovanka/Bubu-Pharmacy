from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^filter/(?P<column>[\w-]+)/(?P<value>[\w-]+)$', views.filterData, name='filter')
]
