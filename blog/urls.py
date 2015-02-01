from django.conf.urls import patterns, url, include
from rest_framework import routers

from blog import views
from blog.models import Article
from blog.apimodels import *

## API related routes
router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<article_id>\d+)/$', views.detail, name='detail'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^admin/add$', views.addPost, name='addPost'),
    url(r'^admin/(?P<article_id>\d+)/$', views.editPost, name='editPost'),
    url(r'^admin/savePost$', views.savePost, name='savePost'),
    url(r'^api/', include(router.urls)),
)
