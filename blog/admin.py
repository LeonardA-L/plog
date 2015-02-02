from django.contrib import admin

# Register your models here.
from blog.models import *

# For testing purpose
admin.site.register(Article)
admin.site.register(Comment)