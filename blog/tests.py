from django.test import TestCase
from datetime import datetime, timedelta
from django.utils.dateparse import parse_date

from blog.models import Article
from blog.tools import *

# Create your tests here.

class ArticleTests(TestCase):
	def test_future_article_will_be_public(self):
		p = Article(title='test', content='test', draft=False, date = datetime.today() + timedelta(days=30), commentable=True)
		p.save()
		lbp = retrieveArticles(limit=-1, drafts=False, future=False)
		contained = p in lbp
		p.delete()
		self.assertEqual(contained, False)

	def test_draft_article_will_be_public(self):
		p = Article(title='test', content='test', draft=True, date = datetime.today() - timedelta(days=30), commentable=True)
		p.save()
		lbp = retrieveArticles(limit=-1, drafts=False, future=False)
		contained = p in lbp
		p.delete()
		self.assertEqual(contained, False)

	def test_todays_article_will_be_public(self):
		p = Article(title='test', content='test', draft=False, date = datetime.today(), commentable=True)
		p.save()
		lbp = retrieveArticles(limit=-1, drafts=False, future=False)
		contained = p in lbp
		p.delete()
		self.assertEqual(contained, True)