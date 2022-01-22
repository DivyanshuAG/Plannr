from django.urls import path, include
from . import views
from week.views import weekView


urlpatterns = [
    path('<slug:name>', views.monthView, name='monthView'),
    path('week', include('week.urls'))
]


