from datetime import datetime

from blog.models import Article

def retrieveArticles(limit, drafts, future):
    latest_blog_posts = Article.objects.all()
    if drafts == False:
        latest_blog_posts = latest_blog_posts.filter(draft = False)
    if future == False:
        latest_blog_posts = latest_blog_posts.filter(date__lte = datetime.today())
    latest_blog_posts = latest_blog_posts.order_by('-date')
    if limit>0:
        latest_blog_posts = latest_blog_posts[:limit]
    return latest_blog_posts

