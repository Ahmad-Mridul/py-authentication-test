from django.urls import path
from . import views
urlpatterns = [
    path('members/',views.members,name='members'),
    path('',views.main,name='main'),
    path('members/details/<slug:slug>',views.details,name='details'),
    path('test',views.testing,name='testing'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]
