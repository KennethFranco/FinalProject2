from django.contrib import admin
from .models import Account, Customer, Food, Order
# Register your models here.

admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(Food)
admin.site.register(Order)
