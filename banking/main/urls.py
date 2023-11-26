from django.urls import path
from .views import *




urlpatterns =[
    path('', index,name="home"),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('after_login/', after_login, name='after_login'),
    path('logout/', logout_view, name='logout'), 
    path('after_login/load_branches/',load_branches,name='load_branches'),
    path('mediator',mediator,name="middle")
]