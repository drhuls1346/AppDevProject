from django.conf.urls import patterns, include, url
from .views import HomeView, Add_ItemView, Remove_ItemView, Update_ItemView, Check_Out_ItemView, Check_In_ItemView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc.views.home', name='home'),
    # url(r'^gisc/', include('gisc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^home$', HomeView.as_view(), name='Home'),
    url(r'^add_item$', Add_ItemView.as_view(), name='Add Item'),
    url(r'^remove_item$', Remove_ItemView.as_view(), name='Remove Item'),
    url(r'^update_item$', Update_ItemView.as_view(), name='Update Item'),
    url(r'^check_out_item$', Check_Out_ItemView.as_view(), name='Check Out Item'),
    url(r'^check_in_item$', Check_In_ItemView.as_view(), name='Check In Item'),
)

