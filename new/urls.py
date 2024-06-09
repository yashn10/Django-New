from django.contrib import admin
from django.urls import path, include
from new import views

urlpatterns = [

    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('checkout/<int:id>', views.checkout, name='checkout'),
    path('checkout/', views.checkouts, name='checkouts'),
    path('shop/', views.shop, name='shop'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:id>/', views.update_cart, name='update_cart'),

]