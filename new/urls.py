from django.contrib import admin
from django.urls import path, include
from new import views

urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('checkout/<int:id>', views.checkout, name='checkout'),
    path('shop/', views.shop, name='shop'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search, name='search')

]