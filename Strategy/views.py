from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Strategy.models import strategy
from Users.models import Profile
# Create your views here.


# strategies listing , default listing with bull and normal strategies
def listing(request, category='bull', level='normal'):
    # identify the session whether has already logined
    if request.user.is_authenticated():
        username = request.user.username

    # list constants
    CATELOG_LIST = ['bull', 'bear']
    LEVEL_LIST = ['normal', 'golden', 'platinum', 'diamond']

    # identify wether the category and level parameter exist
    if(category in CATELOG_LIST and level in LEVEL_LIST):
            # getting strategies with selecting category and level
        try:
            result_list = strategy.objects.filter(category=category, level=level)
        except:
            messages.add_message(request, messages.WARNING, '.')
    else:
        messages.add_message(request, messages.WARNING, '找不到符合的策略類別.')

    return render(request, 'strategies/listing.html', locals())


@login_required(login_url='/users/login/')
def details(request, s_id):
    # identify the session whether has already logined
    if request.user.is_authenticated():
        username = request.user.username

    try:
        user = User.objects.get(username = username)
        # get user profile
        user_profile = Profile.objects.get(user = user)
        user_status = user_profile.status
    except:
        user_status = 0

    try:
        results = strategy.objects.get(id=s_id)
        # identify whether getting the data by id
        if results:
            return render(request, 'strategies/details.html', locals())
        else:
            return render(request, 'details.html', locals())
            # messages.add_message(request, messages.WARNING, '策略不存在.')
    except:
        return redirect('/strategies')
