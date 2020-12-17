from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^log/$', views.logTransaksi, name= 'log'),
    url(r'^log/detail/$', views.logDetailTransaction, name= 'detail'),
]
