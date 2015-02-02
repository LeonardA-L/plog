from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from blog.models import Article
from blog.apimodels import ArticleSerializer
from blog.tools import *

@api_view(['GET', 'POST'])
def article_detail(request, id, format=None):
    """
    Retrieve or delete an article
    """
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'POST':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def articles(request):
    latest_blog_posts = retrieveArticles(limit=-1, drafts=False, future=False)
    serializer = ArticleSerializer(latest_blog_posts, many=True)
    return Response(serializer.data)