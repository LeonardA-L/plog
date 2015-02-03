# Serializers for the API
from rest_framework import serializers, viewsets
from datetime import datetime

from blog.models import *
from blog.tools import *

## Serializers 

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content', 'id')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('author', 'date', 'message')

## ViewSets

class ArticlesViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer

