from django.shortcuts import render
from django.contrib.auth import authenticate
from main.models import Contacts
# Create your views here.
def index(request):
    # identify the session whether has already logined
    if request.user.is_authenticated():
        username = request.user.username
    return render(request, 'index.html', locals())


def contacts(request):
    if request.user.is_authenticated():
        username = request.user.username

    if request.method == 'POST':
        # getting the form datas name, email, contents
        name = request.POST['contact_name']
        email = request.POST['contact_email']
        contents = request.POST['contact_contents']
        # storing data into contacts table in database
        datas = Contacts.objects.create(name=name, email=email, contents=contents)
        datas.save()

    return render(request, 'index.html', locals())