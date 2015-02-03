from datetime import datetime

from blog.models import Article

def retrieveArticles(drafts, future, limit=-1):
    """
    Will retrieve and filter articles according to the parameters
    """
    latest_blog_posts = Article.objects.all()
    if drafts == False:
    	# No drafts
        latest_blog_posts = latest_blog_posts.filter(draft = False)
    if future == False:
    	# date less than or equal today's date. That way future articles won't be publicly visible
        latest_blog_posts = latest_blog_posts.filter(date__lte = datetime.today())
    # Ordered by date DESC
    latest_blog_posts = latest_blog_posts.order_by('-date')
    if limit>0:
        latest_blog_posts = latest_blog_posts[:limit]
    return latest_blog_posts

