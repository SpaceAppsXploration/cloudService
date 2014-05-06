from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spaceServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^simulation/', 'chronos.simulate.simulation'),
    url(r'^webapp/home/$', 'webapp.views.homeTEST'),
    url(r'^webapp/start', 'webapp.views.start'),
    url(r'^webapp/go/to/(?P<p_slug>[a-z]+)/$', 'webapp.views.mission'),

    url(r'^clean/', 'chronos.views.clean'),

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
    
    # Test Endpoints
    url(r'^test/db/entities/$', 'chronos.tests.db'),

    url(r'^$', 'chronos.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
