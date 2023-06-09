from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

import requests

# Create your views here.
#decorator to show the profile needs authentication
@login_required
def user_profile(request):
    import requests
    from django.shortcuts import render

    def fetch_posts(request):
            # response = requests.get('https://jsonplaceholder.typicode.com/posts')
            # posts = response.json()
            # context = {
            #     'posts': posts
            # }
            # return render(request, 'posts.html', context=context)
        return render(request, 'account.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"