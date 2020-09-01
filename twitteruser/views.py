from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from twitteruser.forms import SignupForm
from twitteruser.models import TwitterUser

# Create your views here.
@login_required
def index_view(request):
    return render(request, 'index.html')

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