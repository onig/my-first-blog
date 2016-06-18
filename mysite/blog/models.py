from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    blog_genre = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now) 
    published_date=models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey('auth.User')
    
def published_date(self):
    self.published_date= timezone.now()
    self.save()
    
    
def __str__(self):
    return self.title
    

