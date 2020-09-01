from django.shortcuts import render, HttpResponseRedirect, reverse
from authentication.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from twitteruser.models import TwitterUser


# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get('password')) 
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


