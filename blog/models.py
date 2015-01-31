from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateTimeField('date published')
    draft = models.BooleanField()
    def __str__(self):              # __unicode__ on Python 2
        return self.title