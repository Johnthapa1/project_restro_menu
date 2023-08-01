from django.urls import path
from app_customers import views as customer_views
urlpatterns =[
    path('create/', customer_views.create_customer, name='create_customer'),
    path('edit/', customer_views.edit_customer, name='edit_customer'),
    path('index/', customer_views.index_customer, name='index_customer'),
    path('show/', customer_views.show_customer, name='show_customer')
]