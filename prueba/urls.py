from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from principal.views import PublicidadCreateView

admin.autodiscover()

urlpatterns = patterns('',

	url(r'Crear/',PublicidadCreateView.as_view(),name='Crear_publicidad'),
   	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  	url(r'^admin/', include(admin.site.urls)),
  	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
)