from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name='code/home.html'), name='home'),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^code/', include('code.urls', namespace="code")),
	url(r'^admin/', include(admin.site.urls)),
)
