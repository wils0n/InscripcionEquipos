from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app1.views.home', name='vista_principal'),
    url(r'^principal/$', 'app1.views.home', name='vista_principal'),
    url(r'^registro/$', 'app1.views.registrarse', name='vista_registrarse'),
    url(r'^equipos/$', 'app1.views.equipos', name='vista_equipos'),
    url(r'^bases/$', 'app1.views.basesConcurso', name='vista_bases'),

    url(r'^admin/', include(admin.site.urls)),
)
