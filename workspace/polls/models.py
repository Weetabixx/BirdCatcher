from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here
@python_2_unicode_compatible

class twitter(models.Model):
    tweet_profile_picture = models.CharField(max_length=200)
    tweet_hashtag = models.CharField(max_length=200)
    tweet_text = models.CharField(max_length=141)
    tweet_expand_url = models.CharField(max_length=141)
    tweet_image = models.CharField(max_length=200)
    def __str__(self):
        return self.twitter