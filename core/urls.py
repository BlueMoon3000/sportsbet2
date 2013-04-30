from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from core.views import DirectTemplateView

import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^$', DirectTemplateView.as_view(template_name='index.html', extra_context={'environ':settings.ENVIRONMENT})),
    url(r'^home$', DirectTemplateView.as_view(template_name='index.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('core.api.urls')),
    url(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'public'}),
)
