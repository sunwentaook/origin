from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register,name='registers'),
    url(r'^register_handle/$',views.register_handle,name='register_handle'),
    url(r'^login/$',views.login,name='login'),
    url(r'^login_handle',views.login_handle,name='login_handle'),
    url(r'^logout/',views.logout,name='logout')
]