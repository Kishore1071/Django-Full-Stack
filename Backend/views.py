from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *


def LogIn(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['user_password']

        user = authenticate(username = username, password = password)

        if user is not None:

            login(request, user)

            return redirect('/dashboard/')

        else:

            messages.error(request, "No user found with the given credentials")
            return redirect('/')

    return render(request, 'login.html')

def Signup(request):

    if request.method == "POST":

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email_address']
        create_password = request.POST['create_password']
        confirm_password = request.POST['confirm_password']

        if create_password == confirm_password:

            new_user = User(username = username, email = email, first_name = first_name, last_name = last_name)

            new_user.set_password(create_password)

            new_user.save()

            messages.success(request, "Your account is created.")

            return redirect('/')
        
        else:

            messages.error(request, "Password didn't match.")

    return render(request, 'signup.html')

def Logout(request):

    logout(request)

    messages.success(request, "Logged Out Successfully")

    return redirect('/')


def Dashboard(request):

    all_customer_data = []

    customers = Customer.objects.all()

    for customer in customers:

        customer_orders = Order.objects.filter(customer_id = customer.id)

        customer_data = {
            'customer_id': customer.id,
            'customer_name': customer.customer_name,
            'total_orders': customer_orders.count(),
            'pending_order': customer_orders.filter(status = 0).count(),
            'out_for_delivery': customer_orders.filter(status = 1).count(),
            'delivered': customer_orders.filter(status = 2).count()
        }

        if customer_orders.count() > 0:

            all_customer_data.append(customer_data)

    all_customers = sorted(all_customer_data, key = lambda x: x['total_orders'])

    return render(request, 'dashboard.html', {"username": request.user, 'all_customers_data': all_customers[::-1]})

def OrdersToCustomers(request, id):

    all_orders = Order.objects.filter(customer_id = id)
    
    return render(request, 'order.html', {'all_orders': all_orders, 'from_dashboard': True})


def Customers(request):

    all_customers = Customer.objects.all()
    
    return render(request, 'customers.html', {'customer_data': all_customers})

def CustomerAdd(request):

    if request.method == 'POST':

        customer_form = CustomerForm(request.POST)

        if customer_form.is_valid():

            customer_form.save()

            return redirect('/customers/')

    return render(request, 'customer_add.html', {'customer_form': CustomerForm})

def CustomerUpdate(request, id):

    customer = Customer.objects.get(id = id)

    if request.method == 'POST':

        customer_form = CustomerForm(request.POST, instance=customer)

        if customer_form.is_valid():

            customer_form.save()

            return redirect('/customers/')


    customer_form = CustomerForm(instance=customer)

    return render(request, 'customer_add.html', {'customer_form': customer_form})

def CustomerDelete(request, id):

    customer = Customer.objects.get(id = id)

    customer.delete()

    return redirect('/customers/')


def Products(request):

    all_products = Product.objects.all()

    return render(request, 'products.html', {'product_data': all_products})

def ProductAdd(request):

    if request.method == 'POST':

        product_form = ProductForm(request.POST)

        if product_form.is_valid():

            product_form.save()

            return redirect('/products/')

    return render(request, 'product_add.html', {'product_form': ProductForm})

def ProductUpdate(request, id):

    product = Product.objects.get(id = id)

    if request.method == 'POST':

        product_form = ProductForm(request.POST, instance=product)

        if product_form.is_valid():

            product_form.save()

            return redirect('/products/')


    product_form = ProductForm(instance=product)

    return render(request, 'product_add.html', {'product_form': product_form})

def ProductDelete(request, id):

    product = Product.objects.get(id = id)

    product.delete()

    return redirect('/products/')


def Orders(request):

    all_orders = Order.objects.all()

    return render(request, 'order.html', {'all_orders': all_orders, 'from_dashboard': False})

def OrdersAdd(request):

    if request.method == 'POST':

        data = request.POST

        product_data = Product.objects.get(id = data['product'])

        product_amount = product_data.price * int(data['quantity'])

        product_gst_amount = (product_amount * product_data.gst) / 100

        product_bill_amount = product_amount + product_gst_amount

        order = Order(customer_id = data['customer'], product_id = data['product'], order_number = data['order_number'], order_date = data['order_date'], quantity = data['quantity'], amount = product_amount, gst_amount = product_gst_amount, bill_amount = product_bill_amount)

        order.save()

        return redirect('/orders/')

    return render(request, 'order_add.html', {'order_form': OrderForm()})

def OrdersUpdate(request, id):

    order = Order.objects.get(id = id)

    if request.method == 'POST':

        order_filter = Order.objects.filter(id = id)

        data = request.POST

        product_data = Product.objects.get(id = data['product'])

        product_amount = product_data.price * float(data['quantity'])

        product_gst_amount = (product_amount * product_data.gst) / 100

        product_bill_amount = product_amount + product_gst_amount

        order_filter.update(customer_id = data['customer'], product_id = data['product'], order_number = data['order_number'], order_date = data['order_date'], quantity = data['quantity'], amount = product_amount, gst_amount = product_gst_amount, bill_amount = product_bill_amount, status = data['status'])

        return redirect('/orders/')

    return render(request, 'order_add.html', {'order_form': OrderUpdateForm(instance = order)})

def OrdersDelete(request, id):

    order = Order.objects.get(id = id)

    order.delete()

    return redirect('/orders/')












