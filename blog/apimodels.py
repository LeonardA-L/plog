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
    serializer_class = ArticleSerializer
