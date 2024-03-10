from django.contrib import admin
from django.urls import path,include
# from .views import ad_upload
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('ad/<int:pk>/', views.ad_view, name='ad'),
    path('stand/<int:stand_id>/', views.stand_detail_view, name='stand_detail'),
    path('ad/add/', views.ad_add_view, name='ad_add'),
    path('ad/<int:ad_id>/edit/', views.ad_edit_view, name='ad_edit'),
    path('ad/list/', views.ad_list_view, name='ad_list'),
    path('ad/<int:pk>/delete/', views.ad_delete_view, name='ad_delete'),
    path('login_adlist/', views.login_adlist, name='login_adlist'),
    path('logout/', views.logoutuser, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]