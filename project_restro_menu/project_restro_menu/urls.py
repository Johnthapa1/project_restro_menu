"""
URL configuration for project_restro_menu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app_menus import views as menus_views
from app_customers import views as customer_views
from app_accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menus/', menus_views.list_menu, name='menu-list'),
    path('menus/add', menus_views.add_menu, name='menu-add'),
    path('menus/show', menus_views.show_menu, name='menu_show'),
    path('customers/create', customer_views.create_customer, name='create_customer'),
    path('customers/edit', customer_views.edit_customer, name='edit_customer'),
    path('customers/index', customer_views.index_customer, name='index_customer'),
    path('customers/show', customer_views.show_customer, name='show_customer'),
    path('accounts/login', account_views.login_accounts, name='account_login')
    path('accounts/profile', account_views.profile_accounts, name='profile_login')
    path('accounts/register', account_views.register_accounts, name='register_login')

    
]
