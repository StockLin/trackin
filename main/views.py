from django.shortcuts import render
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    # identify the session whether has already logined
    if request.user.is_authenticated():
        username = request.user.username
    return render(request, 'index.html', locals())