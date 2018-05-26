from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$',views.index,name='indexs'),
    url(r'^cart/$',views.cart,name='carts'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^list/(\d+)/$',views.list,name='list'),
    url(r'^place_order/$',views.place_order),
    url(r'^user_center_info/$',views.user_center_info,name='user_center_infos'),
    url(r'^user_center_order/$',views.user_center_order,name='user_center_orders'),
    url(r'^user_center_site/$',views.user_center_site),
    url(r'^base2/$',views.base2),
    url(r'^base2_handle/$',views.base2_handle,name='base2_handle'),
    # url(r'^footer/',views.footer,name='footer')
]