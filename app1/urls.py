from django.urls import path,re_path
from .views import *

app_name='app1'

urlpatterns = [
    path('',display_all,name='home'),
    path('form/',forms,name='forms'),
    path('delete_all/',delete_all),
    path('contact/',contact,name='contact'),
    path('house_detail/<int:id>',house_detail,name='house_detail'),
    path('delete/',delete_one,name='delete'),
    path('create_user/',create_user,name='create_user'),
    path('login_user/',login_user,name='login_user'),
    path('logout_user',logout_user,name='logout_user'),
    path('edit_house/<int:id>',edit_house,name='edit_house')
]
