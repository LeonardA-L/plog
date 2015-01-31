from django.shortcuts import render
from datetime import datetime

from blog.models import Article

def index(request):
    latest_blog_posts = Article.objects.filter(date__lte = datetime.today())	# Do not display posts that are to be published later
    latest_blog_posts = latest_blog_posts.filter(draft = False)
    latest_blog_posts = latest_blog_posts.order_by('-date')[:10]
    context = {'latest_blog_posts': latest_blog_posts}
    return render(request, 'blog/index.html', context)
