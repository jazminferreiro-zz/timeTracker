from django.conf.urls import url

from . import views

app_name = 'timeTracker'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /timeTracker/verDesarrollador/5/
    url(r'^verDesarrollador/(?P<desarrollador_id>[0-9]+)/$', views.verDesarrollador, name='verDesarrollador')
    #url(r'^(?P<proyecto_id>[0-9]+)/verHoras/$', views.verHoras, name='verHoras'),
]

	