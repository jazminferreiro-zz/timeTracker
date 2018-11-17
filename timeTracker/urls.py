from django.conf.urls import url

from . import views

app_name = 'timeTracker'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<proyecto_id>[0-9]+)/$', views.verTareas, name='verTareas'),
    #url(r'^(?P<proyecto_id>[0-9]+)/verHoras/$', views.verHoras, name='verHoras'),
]

	