from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser

# Create your models here.
class Tweet(models.Model):
    description = models.TextField(max_length=140)
    time_dates = models.DateTimeField(default=timezone.now)
    tweet_maker = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name='tweet_maker')