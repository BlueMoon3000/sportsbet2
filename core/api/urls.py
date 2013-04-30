from django.conf.urls.defaults import *
from core.api.base import APIBase

urlpatterns = patterns('',
    (r'^v(?P<version>\d+)/(?P<model>\w+)/(?P<id>\w+)', APIBase.as_view()),
    (r'^v(?P<version>\d+)/(?P<model>\w+)', APIBase.as_view()),
)
