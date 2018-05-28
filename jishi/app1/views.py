from _sha1 import sha1
from django.shortcuts import render,redirect
from app1.models import UserInfo
from django.http import HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.
def login(request):
    return render(request,'login.html')

def login_handle(request):
    uname = request.POST.get('uname')
    upwd = request.POST.get('upwd')
    request.session['uname'] = request.POST['uname']

    if upwd:
        s2 = sha1()
        s2.update(upwd.encode('utf8'))
        upwd2 = s2.hexdigest()
        userResult = UserInfo.objects.filter(uname=uname,upwd=upwd2)
        if userResult:
            return redirect(reverse('user:liuyanban'))

def register(request):
    return render(request,'register.html')

def register_handle(request):
    uname = request.POST.get('uname')
    upwd = request.POST.get('upwd1')
    upwd2 = request.POST.get('upwd2')
    uemail = request.POST.get('uemail')
    filterResult = UserInfo.objects.filter(uname=uname)
    if filterResult:
        return HttpResponse('用户名已存在')
    else:
        if upwd == upwd2:
            s1 = sha1()
            s1.update(upwd.encode('utf8'))
            upwd3 = s1.hexdigest()
            UserInfo.objects.create(uname=uname, upwd=upwd3, uemail=uemail)
            return render(request,'login.html')

        else:
            return HttpResponse('两次密码不一致')

def liuyanban(request):
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/logout">退出</a>'
        return render(request,'liuyanban.html',{'uname':uname,'uuu':uuu})
    else:
        uname = '<a href="/user/login/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        return render(request, 'liuyanban.html', {'uname': uname, 'uuu': uuu})

def liuyanban_handle(request):
    uname = request.POST.get('uname')
    uemail = request.POST.get('uemail')
    uaddree = request.POST.get('uaddree')
    uliuyan = request.POST.get('uliuyan')
    filterResult = UserInfo.objects.filter(uname=uname)
    if filterResult:
        UserInfo.objects.create(uaddree=uaddree,uliuyan=uliuyan)
        return redirect(reverse('user:base'))
    else:
        return redirect(reverse('user:liuyanban'))

def base(request):
    uliuyan = UserInfo.objects.all()
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/logout">退出</a>'
        return render(request,'base.html',{'uname':uname,'uuu':uuu,'uliuyan':uliuyan})
    else:
        uname = '<a href="/user/login/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        return render(request, 'base.html', {'uname': uname, 'uuu': uuu})

def logout(request):
    request.session.flush()
    return redirect(reverse('user:login'))