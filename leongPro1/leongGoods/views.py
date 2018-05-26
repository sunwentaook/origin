from django.shortcuts import render,redirect
import os
from django.conf import settings
from leongGoods.models import *
from django.http import HttpResponse
# Create your views here.
def index(request):
    a = GoodsInfo.objects.filter(gtype=1)
    a = a[0:4:1]
    b = GoodsInfo.objects.filter(gtype=9)
    b = b[0:4:1]
    c = GoodsInfo.objects.filter(gtype=10)
    c = c[0:4:1]
    d = GoodsInfo.objects.filter(gtype=11)
    d = d[0:4:1]
    e = GoodsInfo.objects.filter(gtype=12)
    e = e[0:4:1]
    f = GoodsInfo.objects.filter(gtype=13)
    f = f[0:4:1]
    a1 = TypeInfo.objects.filter(id=1)
    a2 = TypeInfo.objects.filter(id=9)
    a3 = TypeInfo.objects.filter(id=10)
    a4 = TypeInfo.objects.filter(id=11)
    a5 = TypeInfo.objects.filter(id=12)
    a6 = TypeInfo.objects.filter(id=13)
    # uname = request.session.get('uname')
    # context = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'a1': a1, 'a2': a2, 'a3': a3, 'a4': a4, 'a5': a5,
    #            'a6': a6,'uname':uname}
    # return render(request,'index.html',context)
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/logout">退出</a>'
        chao = '<a href="/goods/cart/">购物车</a>'
        zhongxin = '<a href="/goods/user_center_info/">用户中心</a>'
        dingdan = '<a href="/goods/user_center_site/">全部订单</a>'
        # suoyou = Gouwu.objects.filter(uname=uname)
        # shu = len(suoyou)

        context = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'a1': a1, 'a2': a2, 'a3': a3, 'a4': a4,
                   'a5': a5, 'a6': a6, 'dingdan': dingdan, 'uname': uname, 'uuu': uuu, 'chao': chao,
                   'zhongxin': zhongxin}
    else:
        uname = '<a href="/user/login/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        chao = '<a href="/user/cart/">购物车</a>'
        zhongxin = '<a href="/user/user_center_info/">用户中心</a>'
        dingdan = '<a href="/user/user_center_site/">全部订单</a>'
        # shu = []
        context = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'a1': a1,
                   'a2': a2, 'a3': a3, 'dingdan': dingdan, 'a4': a4, 'a5': a5, 'a6': a6, 'uname': uname, 'uuu': uuu,
                   'chao': chao, 'zhongxin': zhongxin}
    return render(request, 'index.html', context)


def cart(request):
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/logout">退出</a>'
        chao = '<a href="/goods/cart/">购物车</a>'
        zhongxin = '<a href="/goods/user_center_info/">用户中心</a>'
        dingdan = '<a href="/goods/user_center_site/">全部订单</a>'
    else:
        uname = '<a href="/user/login/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        chao = '<a href="/user/cart/">购物车</a>'
        zhongxin = '<a href="/user/user_center_info/">用户中心</a>'
        dingdan = '<a href="/user/user_center_site/">全部订单</a>'
    return render(request,'cart.html',{'uname':uname,'dingdan':dingdan,'uuu':uuu,'chao':chao,'zhongxin':zhongxin})

def detail(request,a):
    b = GoodsInfo.objects.filter(id=a)
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/logout">退出</a>'
        chao = '<a href="/goods/cart/">购物车</a>'
        zhongxin = '<a href="/goods/user_center_info/">用户中心</a>'
        dingdan = '<a href="/goods/user_center_site/">全部订单</a>'
    else:
        uname = '<a href="/user/login/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        chao = '<a href="/user/cart/">购物车</a>'
        zhongxin = '<a href="/user/user_center_info/">用户中心</a>'
        dingdan = '<a href="/user/user_center_site/">全部订单</a>'
    return render(request,'detail.html',{'b':b,'uname':uname,'dingdan':dingdan,'uuu':uuu,'chao':chao,'zhongxin':zhongxin})

def list(request,a):
    if int(a) == 1:
        c = TypeInfo.objects.filter(id=1)
        b = GoodsInfo.objects.filter(gtype=1)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/logout">退出</a>'
            chao = '<a href="/goods/cart/">购物车</a>'
            zhongxin = '<a href="/goods/user_center_info/">用户中心</a>'
            dingdan = '<a href="/goods/user_center_site/">全部订单</a>'
        else:
            uname = '<a href="/user/login/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/cart/">购物车</a>'
            zhongxin = '<a href="/user/user_center_info/">用户中心</a>'
            dingdan = '<a href="/user/user_center_site/">全部订单</a>'
        return render(request, 'list.html', {'b': b, 'a': a,'c':c,'uname':uname,'dingdan':dingdan,'uuu':uuu,'chao':chao,'zhongxin':zhongxin})
    elif int(a) == 2:
        c = TypeInfo.objects.filter(id=9)
        b = GoodsInfo.objects.filter(gtype=9)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/logout">退出</a>'
            chao = '<a href="/goods/cart/">购物车</a>'
            zhongxin = '<a href="/goods/user_center_info/">用户中心</a>'
            dingdan = '<a href="/goods/user_center_site/">全部订单</a>'
        else:
            uname = '<a href="/user/login/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/cart/">购物车</a>'
            zhongxin = '<a href="/user/user_center_info/">用户中心</a>'
            dingdan = '<a href="/user/user_center_site/">全部订单</a>'
        return render(request, 'list.html', {'b': b, 'a': a,'c':c,'uname':uname,'dingdan':dingdan,'uuu':uuu,'chao':chao,'zhongxin':zhongxin})
    elif int(a) == 3:
        c = TypeInfo.objects.filter(id=10)
        b = GoodsInfo.objects.filter(gtype=10)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/logout">退出</a>'
            chao = '<a href="/goods/cart/">购物车</a>'
            zhongxin = '<a href="/goods/user_center_info/">用户中心</a>'
            dingdan = '<a href="/goods/user_center_site/">全部订单</a>'
        else:
            uname = '<a href="/user/login/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/cart/">购物车</a>'
            zhongxin = '<a href="/user/user_center_info/">用户中心</a>'
            dingdan = '<a href="/user/user_center_site/">全部订单</a>'
        return render(request, 'list.html', {'b': b, 'a': a,'c':c,'uname':uname,'dingdan':dingdan,'uuu':uuu,'chao':chao,'zhongxin':zhongxin})

    elif int(a) == 4:
        c = TypeInfo.objects.filter(id=11)
        b = GoodsInfo.objects.filter(gtype=11)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/logout">退出</a>'
            chao = '<a href="/goods/cart/">购物车</a>'
            zhongxin = '<a href="/goods/user_center_info/">用户中心</a>'
            dingdan = '<a href="/goods/user_center_site/">全部订单</a>'
        else:
            uname = '<a href="/user/login/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/cart/">购物车</a>'
            zhongxin = '<a href="/user/user_center_info/">用户中心</a>'
            dingdan = '<a href="/user/user_center_site/">全部订单</a>'
        return render(request, 'list.html', {'b': b, 'a': a,'c':c,'uname':uname,'dingdan':dingdan,'uuu':uuu,'chao':chao,'zhongxin':zhongxin})

    elif int(a) == 5:
        c = TypeInfo.objects.filter(id=12)
        b = GoodsInfo.objects.filter(gtype=12)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/logout">退出</a>'
            chao = '<a href="/goods/cart/">购物车</a>'
            zhongxin = '<a href="/goods/user_center_info/">用户中心</a>'
            dingdan = '<a href="/goods/user_center_site/">全部订单</a>'
        else:
            uname = '<a href="/user/login/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/cart/">购物车</a>'
            zhongxin = '<a href="/user/user_center_info/">用户中心</a>'
            dingdan = '<a href="/user/user_center_site/">全部订单</a>'
        return render(request, 'list.html', {'b': b, 'a': a,'c':c,'uname':uname,'dingdan':dingdan,'uuu':uuu,'chao':chao,'zhongxin':zhongxin})

    elif int(a) == 6:
        c = TypeInfo.objects.filter(id=13)
        b = GoodsInfo.objects.filter(gtype=13)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/logout">退出</a>'
            chao = '<a href="/goods/cart/">购物车</a>'
            zhongxin = '<a href="/goods/user_center_info/">用户中心</a>'
            dingdan = '<a href="/goods/user_center_site/">全部订单</a>'
        else:
            uname = '<a href="/user/login/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/cart/">购物车</a>'
            zhongxin = '<a href="/user/user_center_info/">用户中心</a>'
            dingdan = '<a href="/user/user_center_site/">全部订单</a>'
        return render(request, 'list.html', {'b': b, 'a': a,'c':c,'uname':uname,'dingdan':dingdan,'uuu':uuu,'chao':chao,'zhongxin':zhongxin})
    # return render(request,'list.html')

def place_order(request):
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/logout">退出</a>'
        chao = '<a href="/goods/cart/">购物车</a>'
        zhongxin = '<a href="/goods/user_center_info/">用户中心</a>'
        dingdan = '<a href="/goods/user_center_site/">全部订单</a>'
    else:
        uname = '<a href="/user/login/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        chao = '<a href="/user/cart/">购物车</a>'
        zhongxin = '<a href="/user/user_center_info/">用户中心</a>'
        dingdan = '<a href="/user/user_center_site/">全部订单</a>'
    return render(request,'place_order.html',{'uname':uname,'dingdan':dingdan,'uuu':uuu,'chao':chao,'zhongxin':zhongxin})

def user_center_info(request):
    return render(request,'user_center_info.html')

def user_center_order(request):
    return render(request,'user_center_order.html')

def user_center_site(request):
    return render(request,'user_center_site.html')

def base2(request):
    return render(request,'base2.html')

def base2_handle(request):
    ttitle = request.POST['ttitle']
    gtitle = request.POST['gtitle']
    gprice = request.POST['gprice']
    gunit = request.POST['gunit']
    pic1 = request.FILES.get('gpic')
    picName = os.path.join(settings.MEDIA_ROOT, pic1.name)
    TypeInfo.objects.create(ttitle=ttitle)
    # a = TypeInfo.objects.get(id)
    GoodsInfo.objects.create(gtitle=gtitle,gprice=gprice,gunit=gunit,gpic=picName)
    return HttpResponse('添加成功')


def jisuan(request,d):
    b = GoodsInfo.objects.filter(id=d)
    a = len(b)
    number = request.POST['number']
    price = request.POST['price']
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/logout">退出</a>'
        chao = '<a href="/goods/cart/">购物车</a>'
        zhongxin = '<a href="/goods/user_center_info/">用户中心</a>'
        dingdan = '<a href="/goods/user_center_site/">全部订单</a>'
    else:
        uname = '<a href="/user/login/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        chao = '<a href="/user/cart/">购物车</a>'
        zhongxin = '<a href="/user/user_center_info/">用户中心</a>'
        dingdan = '<a href="/user/user_center_site/">全部订单</a>'
    return render(request,'place_order.html',{'dingdan':dingdan,'number':number,'price':price,'b':b,'a':a,'uname':uname,'uuu':uuu,'chao':chao,'zhongxin':zhongxin})


def jiaru(request,f):
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/logout/">退出</a>'
        chao = '<a href="/goods/cart/">购物车</a>'
        zhongxin = '<a href="/goods/user_center_info/">用户中心</a>'
        dingdan = '<a href="/goods/user_center_site/">全部订单</a>'
        unumber = f
        int(unumber)
        list = GoodsInfo.objects.filter(id=unumber)
        duixiang = list[0]
        unumber = duixiang.id
        unumber = int(unumber)
        utitle = duixiang.gtitle
        udanjia = duixiang.gprice
        udanjia = float(udanjia)
        upic = duixiang.gpic
        ushuliang = request.POST['ushuliang']
        print(ushuliang)
        uprice = request.POST['uprice']
        uprice = float(uprice)
        Gouwu.objects.create(uname=uname, utitle=utitle, ushu=ushuliang, uprice=uprice, unumber=unumber,
                             udanjia=udanjia, upic=upic)
        return render(request,'cart.html',{'uname':uname,'dingdan':dingdan,'uuu':uuu,'chao':chao,'zhongxin':zhongxin})
    else:
        return redirect('/user/login/')
