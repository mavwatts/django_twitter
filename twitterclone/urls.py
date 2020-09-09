"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitteruser import views as main_view
from tweet import views as tweet_view
from notification import views as notifications
from authentication import views as authentication_view


urlpatterns = [
    path('', main_view.index_view, name='homepage'),
    path('login/', authentication_view.login_view),
    path('logout/', authentication_view.logout_view),
    path('signup/', main_view.signup_view),
    # path('tweet/<int:tweet_id>/', tweet_view.tweet_detail_view), 
    path('tweet/<int:tweet_id>/',tweet_view.TweetDetailView.as_view()),
    # path('profile/<int:user_id>/', main_view.profile_view), 
    path('profile/<int:user_id>/', main_view.ProfileView.as_view()), 
    # path('add_tweet/', tweet_view.add_tweet_view),
    path( "add_tweet/" ,tweet_view.AddTweetView.as_view()),
    path('notifications/', notifications.notification_view),
    # path('following/<int:follow_id>/', main_view.following_view),
    path('following/<int:follow_id>/', main_view.FollowingView.as_view()),
    # path('unfollowing/<int:unfollow_id>/', main_view.unfollowing_view),
    path('unfollowing/<int:unfollow_id>/', main_view.UnfollowingView.as_view()),
    path('admin/', admin.site.urls),
]
