from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Strategy.models import strategy
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
        except Exception as e:
            messages.add_message(request, messages.WARNING, '.')
    else:
        messages.add_message(request, messages.WARNING, '找不到符合的策略類別.')

    return render(request, 'strategies/listing.html', locals())
