from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('login/',views.login),
    path('logout/',views.logout),
    path('create_users/',views.create_users),
    path('home/',views.home),
    path('apply/',views.apply),
    path('view_app/',views.view_app),
    path('approve/',views.approve),
    path('view_users/',views.users_list),
    path('user_status/',views.user_status),
    path('applications/',views.applications),
]