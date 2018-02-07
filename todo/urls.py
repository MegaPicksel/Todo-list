from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    url(r'^login/$', views.login_page, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('registration_redirect/', views.registration_redirect, name='registration_redirect'),
    path('api/', views.ToDoView.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/', views.ToDoDetail.as_view()),
]