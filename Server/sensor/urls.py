from django.conf.urls import url

from . import views

app_name = 'sensor'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^fire/$', views.fire, name='fire'),
	url(r'^tremor/$', views.tremor, name='tremor'),
]