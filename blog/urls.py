from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static

from blog import views, apiviews
from blog.apimodels import *


urlpatterns = patterns('',
    # Regular views
    url(r'^$', views.index, name='index'),           # Index list
    url(r'^(?P<start>\d+)/(?P<end>\d+)/$', views.index, name='indexp'),     # Index list with specific start:end page params
    url(r'^(?P<article_id>\d+)/$', views.detail, name='detail'),            # Details on an article (full content, comments)

    # Admin views
    url(r'^admin/$', views.admin, name='admin'),                            # Admin index page
    url(r'^admin/add$', views.addPost, name='addPost'),                     # Calls editPost (see below) with no parameter
    url(r'^admin/(?P<article_id>\d+)/$', views.editPost, name='editPost'),  # Edit or add a blog entry
    url(r'^admin/savePost$', views.savePost, name='savePost'),              # Adds or modifies article then returns admin index page

    # REST framework routes (all objects are returned with a JSON format)
    url(r'^api/articles/(?P<id>[0-9]+)$', apiviews.article_detail),         # GETs a specific article, POST deletes article. Needs article id
    url(r'^api/comment/(?P<id>[0-9]+)$', apiviews.comment),                 # GETs an article's comments. Needs article id
    url(r'^api/articles/$', apiviews.articles),                             # GETs all articles
    url(r'^api/comment/$', apiviews.addComment),                            # POSTs a new comment
    url(r'^api/comment/delete$', apiviews.removeComment),                   # POST : deletes a comment
    # Note : this API is UNSAFE (yet) because it cannot check if the AJAX request you made was made by an administrator (yet).
    
)

#urlpatterns = format_suffix_patterns(urlpatterns)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)
