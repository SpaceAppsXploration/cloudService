from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spaceServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^simulation/', 'xploration.simulate.simulation'),
    url(r'^webapp/start', 'webapp.views.start'),

    url(r'^clean/', 'xploration.views.clean'),

    # REST endpoints
    url(r'^api/docs/', include('rest_framework_swagger.urls')),
    url(r'^api/targets/(?P<t_id>[0-9]+)/$', 'xploration.views.target_detail'),
    url(r'^api/targets/$', 'xploration.views.targets_list'),    
    url(r'^api/missions/details/(?P<m_id>[0-9]+)/$', 'xploration.views.mission_detail'),
    url(r'^api/missions/by/target/(?P<t_id>[0-9]+)/$', 'xploration.views.missions_by_target'),
    url(r'^api/missions/(?P<m_id>[0-9]+)/$', 'xploration.views.single_mission'),
    url(r'^api/missions/$', 'xploration.views.missions_list'),
    url(r'^api/planets/(?P<p_id>[0-9]+)/$', 'xploration.views.single_planet'),
    url(r'^api/planets/$', 'xploration.views.planets_list'),
    url(r'^api/payloads/and/bus/(?P<type_id>[0-9]+)/$', 'xploration.views.single_pb_type'),
    url(r'^api/payloads/and/bus/$', 'xploration.views.pb_list'),
    url(r'^api/components/(?P<c_id>[0-9]+)/$', 'xploration.views.single_component'),
    url(r'^api/components/$', 'xploration.views.components_list'),
    
    # Test Endpoints
    url(r'^test/db/entities/$', 'xploration.tests.db'),

    url(r'^hometest/$', 'xploration.views.homeTEST'),
    url(r'^$', 'xploration.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
