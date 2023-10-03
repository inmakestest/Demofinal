from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path
app_name="schoolapp"

urlpatterns=[
    path('',views.demo,name='demo'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('order_form',views.order_form,name='order_form'),
    path('logout',views.logout,name='logout'),
    path('order_confirmation',views.order_confirmation,name='order_confirmation'),
    path('load_courses', views.load_courses, name='load_courses'),



]
