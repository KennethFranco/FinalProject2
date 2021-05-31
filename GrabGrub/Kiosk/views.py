from typing import NewType
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Account, Customer, Food, Order
import datetime

# Create your views here.

def base(request):
    return render(request, 'Kiosk/base.html')

def login(request):
    if(request.method == "POST"):
        usrnm = request.POST.get('username')
        pwd = request.POST.get('password')

        accountslist = Account.objects.filter(username = usrnm)
        if(len(accountslist) > 0):
            authenticateAccount = Account.objects.get(username = usrnm)
            if(authenticateAccount.getPassword() == pwd):
                global usedaccount
                usedaccount = authenticateAccount
                messages.success(request, 'Successfully Logged In! Welcome to GrabGrub!')
                return redirect('orders')
            else:
                messages.error(request, 'The password you have entered for this account is incorrect.')
                return render(request, 'Kiosk/login.html')
        else:
            messages.error(request, 'The account you are trying to log-in to does not exist.')
            return render(request, 'Kiosk/login.html')

    else:
        return render(request, 'Kiosk/login.html')



def create_account(request):
    if(request.method == "POST"):
        usrnm = request.POST.get('username')
        pswd = request.POST.get('password')
        accountslist = Account.objects.filter(username = usrnm)

        if(len(accountslist) > 0):
            messages.error(request, 'The username you are trying to use is already taken. Please login instead if this is your account.')
            return render(request, 'Kiosk/signup.html')
        else:
            Account.objects.create(username = usrnm, password = pswd)
            messages.success(request, 'Account succesfully created! Please login to continue.')
            return redirect('login')
    else:
        return render(request, 'Kiosk/signup.html')

def home(request):
    order_objects = Order.objects.all()
    return render(request, 'Kiosk/home.html', {'orders':order_objects})

def orders(request):
    order_objects = Order.objects.all()
    return render(request, 'Kiosk/orders.html', {'orders': order_objects})

def add_order(request):  
    food_objects = Food.objects.all()  
    customer_objects = Customer.objects.all()
    if(request.method == "POST"):
        get_customerPK = request.POST.get('customer')
        get_foodPK = request.POST.get('food_item')
        q = request.POST.get('quantity')
        pm = request.POST.get('MOP')
        now = datetime.datetime.now()
        Order.objects.create(order_food=Food.objects.get(pk=get_foodPK), qty=q, ordered_at=now, cust_order=Customer.objects.get(pk=get_customerPK), payment_mode=pm)
        messages.success(request, "Order succesfully created!")
        return redirect('orders')
    else:
        return render(request, 'Kiosk/add_order.html', {'foods':food_objects, 'customers':customer_objects})

def food(request):
    food_objects = Food.objects.all()
    return render(request, 'Kiosk/food.html', {'foods': food_objects})

def add_food(request):
    food_objects = Food.objects.all()
    if(request.method=="POST"):
        check = request.POST.get('food_n')
        match = Food.objects.filter(food_name=check)

        if len(match)> 0:
            messages.error(request, "The food item you are trying to add already exists! Please provide a unique name.")
            return redirect('add_food')
        else:
            n = request.POST.get('food_n')
            d = request.POST.get('food_d')
            p = request.POST.get('food_p')
            now = datetime.datetime.now()
            Food.objects.create(food_name=n,food_description=d,food_price=p,created_at=now)
            messages.success(request, "{}: PHP {} successfully added to the database.".format(n,p))
            return redirect('food')
    else:
        return render(request, "Kiosk/add_food.html", {'foods': food_objects})

def customers(request):
    customer_objects = Customer.objects.all()
    return render(request, 'Kiosk/customers.html', {'customers': customer_objects})

def add_customer(request):
    if(request.method == "POST"):
        n = request.POST.get('customer_n')
        a = request.POST.get('customer_a')
        c = request.POST.get('customer_c')

        Customer.objects.create(customer_name=n, customer_address=a, customer_city=c)
        return redirect('customers')
    else:
        return render(request, "Kiosk/add_customer.html")

def update_customer_details(request, pk):
    customer_objects = Customer.objects.all()
    c = get_object_or_404(Customer, pk=pk) 

    if(request.method=="POST"):
        check = request.POST.get('cn')
        match = Customer.objects.filter(customer_name=check).exclude(pk=pk)

        if len(match) > 0:
            messages.error(request, "The updated name you provided for Customer #{} already exists! Please provide a unique name.".format(c.pk))
            return redirect('customers')
        else:
            c_n = request.POST.get('cn')
            c_a = request.POST.get('ca')
            c_c = request.POST.get('cc')
            Customer.objects.filter(pk=pk).update(customer_name=c_n)
            Customer.objects.filter(pk=pk).update(customer_address=c_a)
            Customer.objects.filter(pk=pk).update(customer_city=c_c)
            messages.success(request, "Customer #{}'s details have been successfully updated. Their name is now {}, their address is now {}, and their city is now {}.".format(c.pk,c_n,c_a,c_c))
            return redirect('customers')
    else:
        return render(request, 'Kiosk/update_customer_details.html', {'c':c, 'customers':customer_objects}) 

def delete_customer(request, pk):
    Customer.objects.filter(pk=pk).delete()
    messages.success(request, "Customer # {} has been deleted from the system.".format(pk))
    return redirect('customers')

def view_order_details(request, pk):
    lia = get_object_or_404(Order, pk=pk) 
    return render(request, 'Kiosk/view_order_details.html', {'lia': lia})

def update_order_details(request, pk):
    lia = get_object_or_404(Order, pk=pk) 

    if(request.method == "POST"):
        q = request.POST.get("qty")
        m = request.POST.get("MOP")

        Order.objects.filter(pk=pk).update(qty=q)
        Order.objects.filter(pk=pk).update(payment_mode=m)
        messages.success(request, "Order #{} successfully updated, Quantity is now {} and Payment Mode is now {}.".format(lia.pk,q,m))
        return redirect('orders')
    else:
        return render(request, 'Kiosk/update_order_details.html', {'lia': lia})

def delete_order(request, pk):
    Order.objects.filter(pk=pk).delete()
    messages.success(request, "Order # {} has been deleted from the system.".format(pk))
    return redirect('orders')

def update_food_details(request,pk):
    food_objects = Food.objects.all()
    f = get_object_or_404(Food, pk=pk) 

    if(request.method=="POST"):
        check = request.POST.get('fn')
        match = Food.objects.filter(food_name=check).exclude(pk=pk)
        # if u want to update other variables only and retain the name

        if len(match) > 0:
            messages.error(request, "The food item you are trying to update to already exists! Please provide a unique name.")
            return redirect('food')
        else:
            f_n = request.POST.get("fn")
            f_d = request.POST.get("fd")
            c_a = request.POST.get("ca")
            pr = request.POST.get("p")

            Food.objects.filter(pk=pk).update(food_name=f_n)
            Food.objects.filter(pk=pk).update(food_description=f_d)
            Food.objects.filter(pk=pk).update(created_at=c_a)
            Food.objects.filter(pk=pk).update(food_price=pr)
            messages.success(request, "Food #{} has been successfully updated. Name is now {}, Description is now {}, Price is now {} and Date of Creation is now {}".format(pk,f_n,f_d,pr,c_a))
            return redirect('food')
    return render(request, 'Kiosk/update_food_details.html', {'f':f, 'foods':food_objects})

def delete_food(request, pk):
    Food.objects.filter(pk=pk).delete()
    messages.success(request, "Food Item # {} has been deleted from the system.".format(pk))
    return redirect('food')