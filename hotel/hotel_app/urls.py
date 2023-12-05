from django.urls import path
from hotel_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/', views.room, name='room'),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('uilchilgee/', views.uilchilgee, name='uilchilgee'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]