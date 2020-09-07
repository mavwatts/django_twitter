from django.db import models
from django.utils import timezone
from tweet.models import Tweet
from twitteruser.models import TwitterUser

# Create your models here.
class Notification(models.Model):
     receiver = models.ForeignKey(TwitterUser, related_name="receiver", on_delete=models.CASCADE, blank=True, null=True)
     msg_content = models.ForeignKey(Tweet, on_delete=models.CASCADE, blank=True, null=True)
     notify_flag = models.BooleanField(default=False)     


