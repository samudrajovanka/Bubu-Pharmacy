from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit/(?P<kode_obat>[\w-]+)/$', views.edit, name='edit'),
    url(r'^filter/(?P<column>[\w-]+)/(?P<value>[\w-]+)$', views.filterData, name='filter'),
]
