from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register', views.register_request, name='register_request'),
    path('login', views.login_request, name='login_request'),
    path('logout', views.logout_request, name='logout_request'),
]
