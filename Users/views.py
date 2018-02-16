from django.shortcuts import render, redirect
from django.conf import settings
import json
import urllib
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
# from .tokens import account_activation_token
from django.core.mail import EmailMessage

# login view definition
def login(request):
    # identify the session whether has already logined
    if request.user.is_authenticated():
        username = request.user.username
        return redirect('/')

    # identify whether the form post datas
    if request.method == 'POST':
        # getting  the user account from login form
        username = request.POST['username']
        # getting the user password from login form
        password = request.POST['userPwd']

        # try to get user by input username and 
        user = authenticate(username = username, password = password)
        # identify whether the user is exist
        if user is not None:
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                messages.success(request, 'New comment added with success!')
                auth.login(request, user)
                messages.add_message(request, messages.SUCCESS, '歡迎來到StocRise投資人交易平台.')
                return redirect('/')
            else:
                messages.add_message(request, messages.WARNING, 'Invalid reCAPTCHA. Please try again.')
                # return HttpResponse('reCAPTCHA Fail!')

        else:
            # 新增錯誤訊息
            messages.add_message(request, messages.WARNING, '帳戶不存在或帳號尚未啟用.')
            return render(request, 'users/login.html', locals())

    return render(request, 'users/login.html', locals())


# logout view definition
def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.SUCCESS, '登出成功.')
    return redirect('/users/login/')