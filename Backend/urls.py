from django.urls import path
from .views import *

urlpatterns = [
    path('', LogIn),
    path('signup/', Signup),
    path('logout/', Logout),

    path('dashboard/', Dashboard),
    path('order/customers/<int:id>/', OrdersToCustomers, name='orders_to_customers'),



    path('customers/', Customers),
    path('customer/add/', CustomerAdd),
    path('customer/update/<int:id>/', CustomerUpdate, name='customer_update'),
    path('customer/delete/<int:id>/', CustomerDelete, name='customer_delete'),

    path('products/', Products),
    path('product/add/', ProductAdd),
    path('product/update/<int:id>/', ProductUpdate, name='product_update'),
    path('product/delete/<int:id>/', ProductDelete, name='product_delete'),

    path('orders/', Orders),
    path('order/add/', OrdersAdd),
    path('order/update/<int:id>/', OrdersUpdate, name='order_update'),
    path('order/delete/<int:id>/', OrdersDelete, name='order_delete'),
]