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
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from Users.models import Profile

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
                # messages.success(request, 'New comment added with success!')
                auth.login(request, user)

                # membership status (會員等級)
                request.session["status"] = Profile.objects.get(user=user).status
                # get user remained day and saved in session(使用者剩餘天數)
                request.session["remainday"] = Profile.objects.get(user=user).remain_day

                # messages.add_message(request, messages.SUCCESS, '歡迎來到StocRise投資人交易平台.')
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



# member sign up
def sign_up(request):
    # identify the session whether has already logined
    if request.user.is_authenticated():
        username = request.user.username
        return redirect('/')

    # getting the post form input datas which for sign up
    if request.method == 'POST':
        username = request.POST['username']     #getting the username from registration.html's from
        useremail = request.POST['useremail']   #getting the user email from registration.html's from
        userPwd = request.POST['userPwd']       #getting the password from registration.html's from
        userCrfm = request.POST['userConPwd']   #getting the confirm from registration.html's from

        # identify whether username has already exist
        if User.objects.filter(username__iexact = username).exists():
            messages.add_message(request, messages.WARNING, '使用者名稱已經存在了，請嘗試使用其他名稱.')

        # if username does not repeat then create new user
        else:
            # identify whether the password and confirm have same values
            if userPwd == userCrfm:
                # create new user
                new_user = User.objects.create_user(username = username, email = useremail, password = userPwd)
                # setting the user aaccount to deactive,before email confirm
                new_user.is_active = False
                # save the change status
                new_user.save()
                # getting the group for user which is memebers
                mem_group = Group.objects.get(name='member_group')
                # add new user to the group
                mem_group.user_set.add(new_user)

                # create user profiles
                user_profiles = Profile.objects.create(user=new_user)
                #email activation for accounts
                current_site = get_current_site(request)
                mail_subject = 'TrackIn - 點擊以下連結進行帳戶開通.'
                message = render_to_string('users/acc_active_email.html', {
                    'user': new_user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(new_user.pk)),
                    'token':account_activation_token.make_token(new_user),
                })
                to_email = new_user.email
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                messages.add_message(request, messages.SUCCESS, '註冊成功，請至您的e-mail進行帳戶啟用.') 
            else:
                messages.add_message(request, messages.WARNING, '請確認密碼與密碼確認是否一致!')
    return render(request, 'users/sign_up.html', locals())  


# email account activation
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect('/')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def membership(request):
    # identify the session whether has already logined
    if request.user.is_authenticated():
        username = request.user.username
        return render(request, 'users/membership.html', locals())


    

    return redirect('/') 
