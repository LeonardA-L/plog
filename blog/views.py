from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.http import Http404, HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.utils.dateparse import parse_date
import math

from blog.models import Article
from blog.tools import *

def index(request, start, end):
    latest_blog_posts = retrieveArticles(limit=-1, drafts=False, future=False)

    articlesPerPage = 10
    totalPages = (len(latest_blog_posts) -1)/articlesPerPage +1
    end = len(latest_blog_posts) if end == -1 else end
    latest_blog_posts = latest_blog_posts[int(start):int(end)]
    
    currentPage = int(start)/articlesPerPage

    context = {
        'latest_blog_posts': latest_blog_posts,
        'articlesPerPage':articlesPerPage,
        'totalPages':range(int(totalPages)),
        'currentPage':currentPage,
        'maximumPage':totalPages,
    }
    return render(request, 'blog/index.html', context)

def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        comments = article.comment_set.all().order_by('date')
    except Article.DoesNotExist:
        raise Http404("Oh noes, your princess is in an other castle.")
    context = {
        'article': article,
        'comments': comments,
    }
    return render(request, 'blog/detail.html', context)

## Admin stuff -- This should probably be somewhere else

def admin(request):
    if request.user.is_superuser:
        #latest_blog_posts = Article.objects.all().order_by('-date')
        latest_blog_posts = retrieveArticles(limit=-1, drafts=True, future=True)
        context = {'latest_blog_posts': latest_blog_posts}
        return render(request, 'blog/admin.html', context)
    else:
        return HttpResponseForbidden()

def addPost(request):
    if request.user.is_superuser:
        return render(request, 'blog/editPost.html', {'date':datetime.today()})
    else:
        return HttpResponseForbidden()

def editPost(request, article_id):
    if request.user.is_superuser:
        try:
            article = Article.objects.get(pk=article_id)
        except Article.DoesNotExist:
            raise Http404("Arr, cap'n, that booty be nowhere.")
        context = {'article': article}
        return render(request, 'blog/editPost.html', context)
    else:
        return HttpResponseForbidden()

def savePost(request):
    if request.user.is_superuser:
        #request.POST['choice']
        draft= True if (request.POST.get('draft', False)=="on" or request.POST.get('draft', False)=="checked") else False
        commentable= True if (request.POST.get('commentable', False)=="on" or request.POST.get('commentable', False)=="checked") else False
        article_id = request.POST.get('article_id', False)
        if article_id:
            p = get_object_or_404(Article, pk=article_id)
            p.title=request.POST['title']
            p.content=request.POST['content']
            p.draft=draft
            p.date = parse_date(request.POST['date'])
            p.commentable = commentable
        else:
            p = Article(title=request.POST['title'], content=request.POST['content'], draft=draft, date = parse_date(request.POST['date']), commentable=commentable)
        p.save()
        return HttpResponseRedirect(reverse('blog:admin'))
    else:
        return HttpResponseForbidden()

# Deprecated, HA!
"""
def deletePost(request):
    p = get_object_or_404(Article, id=request.POST['article_id'])
    p.delete()    
    return HttpResponseRedirect(reverse('blog:admin'))
"""