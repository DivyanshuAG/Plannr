from django.urls import path, include
from . import views

urlpatterns = [
    path('/<int:week>', views.weekView, name='weekView')
]
    