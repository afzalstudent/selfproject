from django.contrib import admin
from django.urls import path, include
from . import views

app_name='selfapp'

urlpatterns = [
   path('',views.home,name='home'),
   path('register/',views.register,name='register'),
   path('login/',views.login,name='login'),
   path('enroll/',views.enroll,name='enroll'),
   path('info/',views.info,name='demo'),
   path('confirm/',views.confirm,name='confirm'),




]
