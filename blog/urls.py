from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^xml$', views.xml, name='xml'),
    url(r'^register/(?P<naam>.+)/(?P<klas>.+)/(?P<regid>.+)/$', views.register, name='register'),
]