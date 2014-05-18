from django.conf.urls import include, patterns, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings

from django.views.decorators.cache import cache_page

from home.views import wphoneregister
from home.views import home
from webapp.views import details_page
from webapp.views import datavis

admin.autodiscover()

urlpatterns = i18n_patterns('',

    url(r'^simulation/', 'chronos.simulate.simulation'),

    
    # REST endpoints
    url(r'^api/docs/', include('rest_framework_swagger.urls')),
    url(r'^api/targets/(?P<t_id>[0-9]+)/$', 'chronos.views.target_detail'),
    url(r'^api/targets/$', 'chronos.views.targets_list'),    
    url(r'^api/missions/details/(?P<m_id>[0-9]+)/$', 'chronos.views.mission_detail'),
    url(r'^api/missions/by/target/(?P<t_id>[0-9]+)/$', 'chronos.views.missions_by_target'),
    url(r'^api/missions/(?P<m_id>[0-9]+)/$', 'chronos.views.single_mission'),
    url(r'^api/missions/$', 'chronos.views.missions_list'),
    url(r'^api/physics/planets/(?P<p_id>[0-9]+)/$', 'chronos.views.single_planet'),
    url(r'^api/physics/planets/$', 'chronos.views.planets_list'),
    url(r'^api/components/types/(?P<type_id>[0-9]+)/$', 'chronos.views.single_pb_type'),
    url(r'^api/components/types/$', 'chronos.views.pb_list'),
    url(r'^api/components/(?P<c_id>[0-9]+)/$', 'chronos.views.single_component'),
    url(r'^api/components/$', 'chronos.views.components_list'),
    
    # home
    url(r'^webapp/wphonebeta/$', cache_page(60 * 180)(wphoneregister)),
    url(r'^about/$', 'home.views.about', name='about'),
    url(r'^promo/$', 'home.views.promo', name='promo'),
    url(r'^$', cache_page(60 * 30)(home), name='home'),

    # Webapp
    url(r'^webapp/home/$', 'webapp.views.homeTEST'),
    url(r'^webapp/start/$', 'webapp.views.start'),
    url(r'^webapp/data/missions/details/(?P<m_id>[0-9]+)/$',  cache_page(60 * 180)(details_page)),
    url(r'^webapp/data/(?P<what>[a-z]+)/$', cache_page(60 * 180)(datavis)),
    url(r'^webapp/go/to/(?P<p_slug>[a-z]+)/to/(?P<m_slug>[a-z_]+)/payload/(?P<pl_slug>[a-z_-]+)/bus/(?P<bus_slug>[a-z_-]+)/$', 'webapp.views.results'),
    url(r'^webapp/go/to/(?P<p_slug>[a-z]+)/to/(?P<m_slug>[a-z_]+)/payload/(?P<pl_slug>[a-z_-]+)/$', 'webapp.views.bus'),
    url(r'^webapp/go/to/(?P<p_slug>[a-z]+)/to/(?P<m_slug>[a-z_]+)/$', 'webapp.views.payload'),
    url(r'^webapp/go/to/(?P<p_slug>[a-z]+)/$', 'webapp.views.mission'),

    #admin and CMS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
