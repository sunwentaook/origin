from _sha1 import sha1
from django.shortcuts import render, redirect
from UserApp.models import *
from django.http import HttpResponse,HttpResponseRedirect
import os
from django.core.urlresolvers import reverse
# from .forms import LoginForm,RegistrationForm


# Create your views here.
def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def register_handle(request):
    uname = request.POST.get('user_name')
    upwd = request.POST.get('pwd')
    upwd2 = request.POST.get('cpwd')
    uemail = request.POST.get('email')
    filterResult = UserInfo.objects.filter(uname=uname)
    if filterResult:
        return HttpResponse('用户名已存在')
    else:
        if upwd == upwd2:
            s1 = sha1()
            s1.update(upwd.encode('utf8'))
            upwd3 = s1.hexdigest()
            UserInfo.objects.create(uname=uname, upwd=upwd3, uemail=uemail)
            return redirect('/user/login')

        else:
            return HttpResponse('两次密码不一致')

def login_handle(request):
    uname = request.POST.get('username')
    upwd = request.POST.get('pwd')
    request.session['uname'] = request.POST['username']

    if upwd:
        s2 = sha1()
        s2.update(upwd.encode('utf8'))
        upwd2 = s2.hexdigest()
        userResult = UserInfo.objects.filter(uname=uname,upwd=upwd2)
        if userResult:
            return redirect(reverse('goods:indexs'))

def logout(request):
    request.session.flush()
    return redirect(reverse('goods:indexs'))