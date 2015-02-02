from django.conf.urls import patterns, url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from blog import views, apiviews
from blog.models import Article
from blog.apimodels import *

"""
## API related routes
router = routers.DefaultRouter()
router.register(r'articles', ArticlesViewSet)
router.register(r'(?P<article_id>\d+)/article', ArticleViewSet)
"""

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<article_id>\d+)/$', views.detail, name='detail'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^admin/add$', views.addPost, name='addPost'),
    url(r'^admin/(?P<article_id>\d+)/$', views.editPost, name='editPost'),
    url(r'^admin/savePost$', views.savePost, name='savePost'),
    url(r'^admin/delete$', views.deletePost, name='deletePost'),
    #url(r'^api/', include(router.urls)),
    url(r'^api/articles/(?P<id>[0-9]+)$', apiviews.article_detail),
)

urlpatterns = format_suffix_patterns(urlpatterns)
