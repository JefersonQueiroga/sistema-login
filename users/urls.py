from django.urls import path
from .views import login_view, logout_view, index

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('index/',index, name='index')
]
