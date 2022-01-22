from django.urls import path, include
from . import views


urlpatterns = [
    path('/', views.monthView, name='monthView'),
    path('/<int:week>', views.weekView, name='weekView')
]


