from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.utils.dateparse import parse_date


from blog.models import Article
from blog.tools import *

def index(request):
    latest_blog_posts = retrieveArticles(limit=10, drafts=False, future=False) 
    context = {'latest_blog_posts': latest_blog_posts}
    return render(request, 'blog/index.html', context)

def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Oh noes, your princess is in an other castle.")
    context = {'article': article}
    return render(request, 'blog/detail.html', context)

## Admin stuff -- This should probably be somewhere else

def admin(request):
    #latest_blog_posts = Article.objects.all().order_by('-date')
    latest_blog_posts = retrieveArticles(limit=-1, drafts=True, future=True)
    context = {'latest_blog_posts': latest_blog_posts}
    return render(request, 'blog/admin.html', context)

def addPost(request):
	return render(request, 'blog/editPost.html', {'date':datetime.today()})

def editPost(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Arr, cap'n, that booty be nowhere.")
	context = {'article': article}
	return render(request, 'blog/editPost.html', context)

def savePost(request):
    #request.POST['choice']
    draft= True if (request.POST.get('draft', False)=="checked") else False
    article_id = request.POST.get('article_id', False)
    if article_id:
    	p = get_object_or_404(Article, pk=article_id)
    	p.title=request.POST['title']
    	p.content=request.POST['content']
    	p.draft=draft
    	p.date = parse_date(request.POST['date'])
    else:
    	p = Article(title=request.POST['title'], content=request.POST['content'], draft=draft, date = parse_date(request.POST['date']))
    p.save()
    return HttpResponseRedirect(reverse('blog:admin'))

def deletePost(request):
    p = get_object_or_404(Article, id=request.POST['article_id'])
    p.delete()    
    return HttpResponseRedirect(reverse('blog:admin'))
