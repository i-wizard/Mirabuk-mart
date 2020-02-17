from django.urls import path

from . import views 

urlpatterns=[
    path("register.html",views.register,name="register"),
    path('login.html', views.login, name='login'),
    path('logout.html', views.logout, name="logout")

]