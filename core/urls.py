from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^home$', TemplateView.as_view(template_name='index.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('core.api.urls')),
    url(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'public'}),
)
