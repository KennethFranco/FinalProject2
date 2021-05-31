"""GrabGrub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name = 'base'),
    path('login/', views.login, name = "login"),
    path('signup/', views.create_account, name = "signup"),
    path('home/', views.home, name = "home"),
    path('orders/', views.orders, name = "orders"),
    path('add_order/', views.add_order, name = "add_order"),
    path('food_items/', views.food, name = "food"),
    path('add_food/', views.add_food, name = "add_food"),
    path('update_food_details/<int:pk>/', views.update_food_details, name = "update_food_details"),
    path('delete_food/<int:pk>/',views.delete_food, name = "delete_food"),
    path('customers/', views.customers, name = "customers"),
    path('add_customer/', views.add_customer, name = "add_customer"),
    path('update_customer_details/<int:pk>/', views.update_customer_details, name = "update_customer_details"),
    path('delete_customer/<int:pk>/', views.delete_customer, name = "delete_customer"),
    path('view_order_details/<int:pk>/', views.view_order_details, name = "view_order_details"),
    path('update_order_details/<int:pk>/', views.update_order_details, name = "update_order_details"),
    path('delete_order/<int:pk>', views.delete_order, name = "delete_order"),
]
