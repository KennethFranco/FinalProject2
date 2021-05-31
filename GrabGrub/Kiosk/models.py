from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    objects = models.Manager()

    def __str__(self):
        return str(self.pk) + ": " + self.username

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

class Customer(models.Model):
    customer_name = models.CharField(max_length=300)
    customer_address = models.CharField(max_length=300)
    customer_city = models.CharField(max_length=300)
    objects = models.Manager()

    def getName(self):
        return str(self.customer_name)

    def getAddress(self):
        return str(self.customer_address)

    def getCity(self):
        return str(self.customer_city)
    
    def __str__(self):
        return "" + self.customer_name + " - " + self.customer_address + ", " + self.customer_city

class Food(models.Model):
    food_name = models.CharField(max_length=300)
    food_description = models.CharField(max_length=300)
    food_price = models.FloatField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(blank = True, null = True)
    objects = models.Manager()

    def getName(self):
        return str(self.food_name)

    def getDesc(self):
        return str(self.food_description)

    def price(self):
        return str(self.food_price)

    def __str__(self):
        return "" + self.food_name + " - " + str(self.food_price) + ", " + self.food_description + " created at: " + str(self.created_at)

payment_methods = (('cash','Cash'), ('card','Card'))

class Order(models.Model):
    order_food = models.ForeignKey(Food, on_delete = models.CASCADE)
    qty = models.FloatField(null = True, blank = True, default = None)
    ordered_at = models.DateTimeField(blank = True, null = True)
    cust_order = models.ForeignKey(Customer, on_delete = models.CASCADE)
    payment_mode = models.CharField(max_length=300, choices=payment_methods)
    objects = models.Manager()

    def getMode(self):
        return str(self.payment_mode)
    
    def getQuantity(self):
        return str(self.qty)

    def __str__(self):
        return "{}x{}, For Customer Name: {}, Paid through {} on {}".format(self.order_food,self.qty,self.cust_order,self.payment_mode,self.ordered_at)