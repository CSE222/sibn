from django.conf.urls import url

from . import views

app_name = 'terminal'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^logs/$', views.logs, name='logs'),
	url(r'^clear/$', views.clear, name='clear'),
]