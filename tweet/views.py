from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification
from django.views.generic.base import View

import re

# Create your views here.
# @login_required
# def add_tweet_view(request):
#     if request.method == 'POST':
#         form = TweetForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             tweet_post = Tweet.objects.create(
#                 tweet=data['tweet'],
#                 tweet_maker=request.user
#             )
#             if "@" in data['tweet']:
#                 recipients = re.findall(r'@(\w+)', data.get("tweet"))
#                 for recipient in recipients:
#                     match_user = TwitterUser.objects.get(username=recipient)
#                     if match_user:
#                         message = Notification.objects.create(msg_content=tweet_post, receiver=match_user)
#             return HttpResponseRedirect(reverse('homepage'))

#     form = TweetForm()
#     return render(request, 'generic_form.html', {'form': form})


class AddTweetView(View):
    def get(self, request):
        form = TweetForm()
        return render(request, 'generic_form.html', {'form': form})

    def post(self, request):
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet_post = Tweet.objects.create(
                tweet=data['tweet'],
                tweet_maker=request.user
            )
            if "@" in data['tweet']:
                recipients = re.findall(r'@(\w+)', data.get("tweet"))
                for recipient in recipients:
                    match_user = TwitterUser.objects.get(username=recipient)
                    if match_user:
                        message = Notification.objects.create(msg_content=tweet_post, receiver=match_user)
            return HttpResponseRedirect(reverse('homepage'))



# def tweet_detail_view(request, tweet_id):
#     comment = Tweet.objects.filter(id=tweet_id).first()
#     return render(request, 'tweet_detail.html', {"comment":comment} )

class TweetDetailView(View):
    def get(self, request, tweet_id):
        comment = Tweet.objects.filter(id=tweet_id).first()
        return render(request, 'tweet_detail.html', {"comment":comment} )


