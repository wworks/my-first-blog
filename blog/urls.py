from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^push/$', views.push, name='push'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^xml$', views.xml, name='xml'),
    #url(r'^register$', views.register, name='register'),
    url(r'^register/(?P<naam>.+)/(?P<klas>.+)/(?P<regid>.+)/$', views.register, name='register'),
]