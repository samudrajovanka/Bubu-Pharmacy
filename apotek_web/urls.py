from django.conf.urls import url, include, handler404
from django.contrib import admin

handler404 = 'apotek_web.views.pageNotFound'

from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^filter/(?P<column>[\w-]+)/(?P<value>[\w-]+)$', views.filterData, name='filter'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^obat/', include('obat.urls', namespace='obat')),
    url(r'^persediaan-obat/', include('persediaan_obat.urls', namespace='persediaan')),
    url(r'^transaksi/', include('transaksi.urls', namespace='transaksi'))
]
