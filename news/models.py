from django.db import models

# Create your models here.
class News(models.Model):
    def __str__(self):
        return self.news_name
    news_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    news_desc = models.TextField(default=None)
