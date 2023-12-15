from django.urls import path
from .views import login_view, logout_view, index, tela_admin,tela_comum

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('administrativa/',tela_admin, name='administrativa'),
    path('comum/',tela_comum, name='comum'),
    path('',index, name='index')
]
