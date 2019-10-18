from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    def __str__(self):
        return self.news_name
    news_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    news_desc = models.TextField(default=None)

    # Add indexing method to News
    def indexing(self):
        obj = NewsPostIndex(meta={'id': self.id}, news_name=self.news_name, pub_date=self.pub_date, news_desc=self.news_desc)
        obj.save()
        return obj.to_dict(include_meta=True)
