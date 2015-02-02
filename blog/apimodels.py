# Serializers for the API
from rest_framework import serializers, viewsets
from datetime import datetime

from blog.models import Article
from blog.tools import *

# Serializers define the API representation.
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content', 'id')

# ViewSets define the view behavior.
class ArticlesViewSet(viewsets.ModelViewSet):
	#latest_blog_posts = Article.objects.filter(date__lte = datetime.today())
	#latest_blog_posts = latest_blog_posts.filter(draft = False)
	#latest_blog_posts = latest_blog_posts.order_by('-date')
	latest_blog_posts = retrieveArticles(limit=-1, drafts=False, future=False)
	queryset = latest_blog_posts
	serializer_class = ArticleSerializer
