from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from blog.models import *
from blog.apimodels import ArticleSerializer, CommentSerializer
from blog.tools import *


@api_view(['GET', 'POST'])
def article_detail(request, id, format=None):
    """
    Retrieves or delete an article
    """
    article = get_object_or_404(Article, pk=id)
    if request.method == 'GET':                                 # GET will return the article (JSON format)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'POST':                              # POST will remove the article (csrf required)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def addComment(request, format=None):
    """
    Posts a comment
    """
    try:
        # Retrieve form fields
        name = request.POST['name']
        quest=request.POST['quest']
        color=request.POST['color']
        message=request.POST['message']
        p = get_object_or_404(Article, pk=request.POST['post_id'])
        if p.commentable:   # If allowed, create new comment
            comment = p.comment_set.create(author=name,quest=quest,color=color,message=message)
    except KeyError:        # Missing value (no author | no message | no color | no quest)
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def removeComment(request, format=None):
    """
    Deletes a comment
    """
    comment = get_object_or_404(Comment, pk=request.POST['comment_id'])
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def comment(request, id, format=None):
    """
    Gets a specific article's comments
    """
    p = get_object_or_404(Article, pk=id)
    serializer = CommentSerializer(p.comment_set.all(), many=True)
    return Response(serializer.data)

@api_view(['GET'])
def articles(request):
    """
    Gets all the public articles
    Only public fields will be serialized. See apimodels.py
    """
    latest_blog_posts = retrieveArticles(drafts=False, future=False)
    serializer = ArticleSerializer(latest_blog_posts, many=True)
    return Response(serializer.data)
