from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin-login/', login_admin, name='login_admin'),
    path('admin-logout/', logout_admin, name='logout-admin'),
    path('admin-register/', admin_register, name='register-admin'),
]
