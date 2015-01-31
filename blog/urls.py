from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<article_id>\d+)/$', views.detail, name='detail'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^admin/add$', views.addPost, name='addPost'),
    url(r'^admin/savePost$', views.savePost, name='savePost'),
)