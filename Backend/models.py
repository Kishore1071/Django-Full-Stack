from django.db import models

class Customer(models.Model):

    customer_name = models.CharField(max_length=200, null=True)
    company_name = models.CharField(max_length=300, null=True)
    location = models.CharField(max_length=200, null=True)


    def __str__(self):

        return self.customer_name
    

class Product(models.Model):

    product_name = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=0)
    gst = models.FloatField(default=0)

    def __str__(self):

        return self.product_name

    
class Order(models.Model):

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    order_number = models.CharField(max_length=200, null=True)
    order_date = models.DateField(null=True)
    quantity = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    gst_amount = models.FloatField(default=0)
    bill_amount = models.FloatField(default=0)

    status_choices = (
        (0, 'Pending'),
        (1, 'Out For Delivery'),
        (2, 'Delivered'),
    )

    status = models.IntegerField(default=0, choices=status_choices)

    def __str__(self):

        return self.customer.customer_name + " " + self.order_number