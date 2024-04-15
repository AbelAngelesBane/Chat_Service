from django.urls import path

from ..views.auth_view import *

urlpatterns_auth = [
    path('auth/register', apiRegisterAccount.as_view(), name="Registration")  
]

