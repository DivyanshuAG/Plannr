from django.urls import path, include
from . import views
from week.views import weekView


urlpatterns = [
    path('<slug:name>', views.monthView, name='monthView'),
    path('<slug:name>/<int:date>', views.dayView, name='dayView'),
    path('inbox/', views.inbox, name='inbox')
]


