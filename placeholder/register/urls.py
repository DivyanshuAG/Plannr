from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.register, name='registerView'),
    path('login', views.login, name='loginView'),
    path('loginSuccess',views.loginSuccess,name='profileView')
]
