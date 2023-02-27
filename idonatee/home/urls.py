from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signout',views.signout,name='signout'),
    path('detail',views.detail, name='detail'),
    path('rdetail',views.rdetail, name='rdetail'),
    path('odetail',views.odetail, name='odetail'),
    path('detail2',views.detail2, name='detail2'),
    path('dashboard',views.dashboard,name='dashboard'),
    ] 