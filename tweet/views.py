from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from tweet.forms import TweetForm
from tweet.models import Tweet


# Create your views here.
@login_required
def add_tweet_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                tweet =data.get('tweet'),
                tweet_maker = request.user
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = TweetForm()
    return render(request, 'generic_form.html', {'form': form})

def tweet_detail_view(request, tweet_id):
    comment = Tweet.objects.filter(id=tweet_id).first()
    return render(request, 'tweet_detail.html', {"comment":comment} )


