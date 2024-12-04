from django.urls import path

import cricketschedule_project.matches.match_list
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('', cricketschedule_project.matches.match_list.match_list, name='match_list'),
    path('add/', views.add_match, name='add_match'),
    path('edit/<int:id>/', views.edit_match, name='edit_match'),
    path('delete/<int:id>/', views.delete_match, name='delete_match'),
]

