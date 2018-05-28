from django.conf.urls import include, url
from app1 import views

urlpatterns = [
    url(r'^login/',views.login,name='login'),
    url(r'^register/',views.register,name='register'),
    url(r'^liuyanban/',views.liuyanban,name='liuyanban'),
    url(r'^login_handle/',views.login_handle,name='login_handle'),
    url(r'^register_handle/',views.register_handle,name='register_handle'),
    url(r'^liuyanban_handle/',views.liuyanban_handle,name='liuyanban_handle'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^base/',views.base,name='base')
]