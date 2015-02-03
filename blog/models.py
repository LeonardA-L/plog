from django.db import models
from datetime import datetime

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    draft = models.BooleanField()                       # a draft article won't be publicly visible
    commentable = models.BooleanField()                 # opens/closes comments on an article
    def __str__(self):
        return self.title

class Comment(models.Model):
	post = models.ForeignKey(Article)
	author = models.CharField(max_length=250)
	quest = models.CharField(max_length=250)
	date = models.DateField(default=datetime.now)
	color = models.CharField(max_length=8)
	message = models.TextField()