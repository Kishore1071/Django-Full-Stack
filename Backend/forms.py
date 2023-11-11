from django import forms
from .models import *


class CustomerForm(forms.ModelForm):

    class Meta:

        model = Customer
        fields = '__all__'

class ProductForm(forms.ModelForm):

    class Meta:

        model = Product
        fields = '__all__'


class OrderForm(forms.ModelForm):

    class Meta:

        model = Order
        fields = ['customer', 'product', 'order_number', 'order_date', 'quantity']


class OrderUpdateForm(forms.ModelForm):

    class Meta:

        model = Order
        fields = ['customer', 'product', 'order_number', 'order_date', 'quantity', 'status']