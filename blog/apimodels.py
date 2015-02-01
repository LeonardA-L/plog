# Serializers for the API
from rest_framework import serializers, viewsets
from datetime import datetime

from blog.models import Article

# Serializers define the API representation.
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content')

# ViewSets define the view behavior.
class ArticleViewSet(viewsets.ModelViewSet):
	latest_blog_posts = Article.objects.filter(date__lte = datetime.today())
	latest_blog_posts = latest_blog_posts.filter(draft = False)
	latest_blog_posts = latest_blog_posts.order_by('-date')
	queryset = latest_blog_posts
	serializer_class = ArticleSerializer