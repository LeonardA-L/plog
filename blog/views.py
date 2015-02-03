from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.http import Http404, HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.dateparse import parse_date

from blog.models import Article
from blog.tools import *

def index(request, start, end):
    """
    Renders the latest articles on the blog, possibly filtered by page
    """

    latest_blog_posts = retrieveArticles(limit=-1, drafts=False, future=False)      # See tools.py

    # Pagination calculations
    articlesPerPage = 10
    totalPages = (len(latest_blog_posts) -1)/articlesPerPage +1
    end = len(latest_blog_posts) if end == -1 else end
    currentPage = int(start)/articlesPerPage

    # Pagination filter
    latest_blog_posts = latest_blog_posts[int(start):int(end)]

    context = {
        'latest_blog_posts': latest_blog_posts,
        'articlesPerPage':articlesPerPage,
        'totalPages':range(int(totalPages)),
        'currentPage':currentPage,
        'maximumPage':totalPages,
    }
    return render(request, 'blog/index.html', context)

def detail(request, article_id):
    """
    Renders complete details on an article (full content, comments)
    """
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

## Admin related views. Should probably have been put in a separate file

def admin(request):
    """
    Renders the admin index page (lists all articles and offers to delete or edit them)
    Checks if user is admin
    """
    if request.user.is_superuser:
        #latest_blog_posts = Article.objects.all().order_by('-date')
        latest_blog_posts = retrieveArticles(limit=-1, drafts=True, future=True)
        context={'latest_blog_posts':latest_blog_posts}
        return render(request, 'blog/admin.html', context)
    else:
        return HttpResponseForbidden()

def addPost(request):
    """
    Renders the "Add new entry" page
    Checks if user is admin
    """
    if request.user.is_superuser:
        return render(request, 'blog/editPost.html', {'date':datetime.today()})
    else:
        return HttpResponseForbidden()

def editPost(request, article_id):
    """
    Renders the "Add new entry" page with an article as parameter, allowing user to edit it
    Checks if user is admin
    """
    if request.user.is_superuser:
        try:
            article = Article.objects.get(pk=article_id)
            comments = article.comment_set.all().order_by('date')
        except Article.DoesNotExist:
            raise Http404("Arr, cap'n, that booty be nowhere.")
        context = {
            'article': article,
            'comments': comments,
        }
        return render(request, 'blog/editPost.html', context)
    else:
        return HttpResponseForbidden()

def savePost(request):
    """
    Saves a post, new or modified
    Checks if user is admin
    """
    if request.user.is_superuser:
        # Calculates checkboxes values
        draft= True if (request.POST.get('draft', False)=="on" or request.POST.get('draft', False)=="checked") else False
        commentable= True if (request.POST.get('commentable', False)=="on" or request.POST.get('commentable', False)=="checked") else False

        article_id = request.POST.get('article_id', False)

        if article_id:      # Modification
            p = get_object_or_404(Article, pk=article_id)
            p.title=request.POST['title']
            p.content=request.POST['content']
            p.draft=draft
            p.date = parse_date(request.POST['date'])
            p.commentable = commentable
        else:               # New article
            p = Article(title=request.POST['title'], content=request.POST['content'], draft=draft, date = parse_date(request.POST['date']), commentable=commentable)
        p.save()
        return HttpResponseRedirect(reverse('blog:admin'))
    else:
        return HttpResponseForbidden()