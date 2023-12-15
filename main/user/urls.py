from django.urls import path
from . import views

urlpatterns = [
    path('login',views.loginpage,name='login'),
    path('signup',views.signup,name='signup'),
    path('',views.home),
    path('items',views.items,name='items'),
    path('logout',views.user_logout,name='user_logout')
]
