from django.conf.urls import url

from . import views

app_name = 'timeTracker'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /timeTracker/detail/5/
    url(r'^detail/(?P<desarrollador_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /timeTracker/detail/5/add/
    url(r'^detail/(?P<desarrollador_id>[0-9]+)/add/$', views.add, name='add'),

]

	