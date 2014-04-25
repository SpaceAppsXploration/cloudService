from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spaceServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^simulation/', 'xploration.views.simulation'),
    url(r'^planets/mars', 'xploration.views.Mars'),
    url(r'^webapp/start', 'webapp.views.start'),

    url(r'^test/', 'xploration.views.test'),
    url(r'^clean/', 'xploration.views.clean'),

    # REST endpoints
    url(r'^targets/$', 'xploration.views.targets_list'),
    url(r'^targets/(?P<t_id>[0-9]+)/$', 'xploration.views.target_detail'),

    url(r'^hometest', 'xploration.views.homeTEST'),
    url(r'^$', 'xploration.views.home', name='home'),
    # url(r'^admin/', include(admin.site.urls)),
)
