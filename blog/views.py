from django.shortcuts import render
from datetime import datetime

from blog.models import Article

def index(request):
    latest_blog_posts = Article.objects.filter(date__lte = datetime.today())
    latest_blog_posts = latest_blog_posts.order_by('-date')[:10]
    context = {'latest_blog_posts': latest_blog_posts}
    return render(request, 'blog/index.html', context)
