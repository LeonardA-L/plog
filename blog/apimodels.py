# Serializers for the API
from rest_framework import serializers, viewsets
from datetime import datetime

from blog.models import *
from blog.tools import *

# Serializers define the API representation.
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content', 'id')

# ViewSets define the view behavior.
class ArticlesViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('author', 'date', 'message')