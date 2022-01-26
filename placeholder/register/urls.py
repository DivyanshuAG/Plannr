from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.register, name='registerView'),
    path('login/', views.loginView, name='loginView'),
    path('logout/', views.logoutView, name="logout"),
    path('password_reset/done/',auth_views.passwordResetViewDoneView.as_View(template_name='../'), name="forgotPasswordView")
]
