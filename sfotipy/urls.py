from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
#from userprofiles.views import LoginView, ProfileView
from artists.views import ArtistDetailView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sfotipy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('userprofiles.urls')),
    (r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracks/(?P<title>[\w\-\W]+)/', 'tracks.views.track_view',
        name='track_view'),
    #url(r'^signup/', 'userprofiles.views.signup', name='signup'),
    #url(r'^signin/', LoginView.as_view(template_name='login.html'), name='login'),
    #url(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    #url(r'^profile/$', ProfileView.as_view(), name='profile.html'),
    url(r'^artists/(?P<pk>[\d]+)', ArtistDetailView.as_view()),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    )
