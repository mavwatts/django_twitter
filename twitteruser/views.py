from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from twitteruser.forms import SignupForm
from twitteruser.models import TwitterUser
from tweet.models import Tweet

# Create your views here.
@login_required
def index_view(request):
    tweets = Tweet.objects.all()
    return render(request, 'index.html', {"tweets": tweets})
    
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                username=data.get('username'), 
                password=data.get('password'), 
            )
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect(reverse('homepage'))

    form = SignupForm()
    return render(request, "generic_form.html", {'form': form})


def profile_view(request, user_id):
    current_user = TwitterUser.objects.filter(id=user_id).first()
    tweets = Tweet.objects.filter(tweet_maker=current_user)
    follow_count = len(current_user.following.all())
    return render(request, 'profile.html', {'current_user': current_user, 'tweets': tweets, 'follow_count': follow_count})

def following_view(request, follow_id):
    logged_in_user = TwitterUser.objects.get(username = request.user.username)
    add_user = TwitterUser.objects.filter(id=follow_id).first()
    logged_in_user.following.add(add_user)
    logged_in_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def unfollowing_view(request, unfollow_id):
    logged_in_user = TwitterUser.objects.get(username = request.user.username)
    remove_user = TwitterUser.objects.filter(id=unfollow_id).first()
    logged_in_user.following.remove(remove_user)
    logged_in_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))