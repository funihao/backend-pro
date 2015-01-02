from django.conf.urls import patterns, url
from userprofiles.views import LoginView, ProfileView, PerfilRedirectView
#from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^profil/$', ProfileView.as_view(), name='profile'),
    url(r'^perfil/$', PerfilRedirectView.as_view(), name='perfil'),
)
