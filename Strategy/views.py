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

    EMPTY_MSG = None

    # identify wether the category and level parameter exist
    if(category in CATELOG_LIST and level in LEVEL_LIST):
            # getting strategies with selecting category and level
        try:
            result_list = strategy.objects.filter(category=category, level=level)
        except:
            result_list = None
            messages.add_message(request, messages.WARNING, '.')
    else:
        messages.add_message(request, messages.WARNING, '找不到符合的策略類別.')

    if result_list != None:
        # result is Empty
        if not result_list:
            EMPTY_MSG = '目前沒有上架策略，敬請期待.'

        paginator = Paginator(result_list, 6)
        page = request.GET.get('page')
        try:
            current_strate = paginator.page(page)
        except PageNotAnInteger:
            current_strate = paginator.page(1)
        except EmptyPage:
            current_strate = paginator.page(paginator.num_page)


    return render(request, 'strategies/listing.html', locals())


@login_required(login_url='/users/login/')
def details(request, s_id):
    # strategies level name to user status dictionary
    LEVEL_DIC = {
        'normal':0,
        'golden':1,
        'platinum':2,
        'diamond':3,
    }

# the constant which can let user see strategy detail
    PASS = None

# save error messages
    ERROR_MSG_HEAD = None
    ERROR_MSG = None

    # identify the session whether has already logined
    if request.user.is_authenticated():
        username = request.user.username


# trying to get use profile
    try:
        user = User.objects.get(username = username)
        # get user profile
        user_profile = Profile.objects.get(user = user)
        user_status = user_profile.status
    except:
        user_status = 0


# trying to get specific strategy by it's id
    try:
        # getting specific strategy by id
        results = strategy.objects.get(id=s_id)
        # transformimg strategies level string to user status numbers by using LEVEL_DIC dictionary
        s_level = LEVEL_DIC[results.level]

    except:
        results = None
        # return redirect('/strategies')


    # identify whether data is gotten by it's id
    if results:
        # identify whether user auth is same as strategies level
        if user_status >= s_level:
            PASS = 1
        else:
            ERROR_MSG_HEAD = '會員等級不足'
            ERROR_MSG = '你的會員等級不足，請升級到指定的會員等級.'
    else:
        ERROR_MSG_HEAD = '頁面連結錯誤'
        ERROR_MSG = '很抱歉！您所要進入的頁面連結可能有誤，您可到其他網頁瀏覽或是使用搜尋功能查詢其他商品資訊。'
        # messages.add_message(request, messages.WARNING, '策略不存在.')

    return render(request, 'strategies/details.html', locals())

