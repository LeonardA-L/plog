from django.shortcuts import render
from datetime import datetime
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader

from blog.models import Article

def index(request):
    latest_blog_posts = Article.objects.filter(date__lte = datetime.today())	# Do not display posts that are to be published later
    latest_blog_posts = latest_blog_posts.filter(draft = False)
    latest_blog_posts = latest_blog_posts.order_by('-date')[:10]
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
    latest_blog_posts = Article.objects.all().order_by('-date')
    context = {'latest_blog_posts': latest_blog_posts}
    return render(request, 'blog/admin.html', context)

def addPost(request):
	return render(request, 'blog/editPost.html', {})

def savePost(request):
    #request.POST['choice']
    p = Article(title=request.POST['title'], content=request.POST['content'], draft=True if request.POST['draft']=="checked" else False)
    p.save()
    return HttpResponseRedirect(reverse('blog:admin'))