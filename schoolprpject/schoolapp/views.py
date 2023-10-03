from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse

from .models import Department, Course, school
from .forms import OrderForm
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def demo(request):
    obj=school.objects.all()
    return render(request,"index.html",{'result':obj})

def order_form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Order Confirmed')

            # Redirect to the order confirmation page
            return redirect(reverse('schoolapp:order_confirmation'))
    else:
        form = OrderForm()

    return render(request, 'order_form.html', {'form': form})

def load_courses(request):
    department_id = request.GET.get('department')
    courses = Course.objects.filter(department_id=department_id).values('id', 'name')
    return JsonResponse(list(courses), safe=False)




def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('schoolapp:order_form')
        else:
            messages.info(request,"invalid")
            return redirect('schoolapp:login')
    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('schoolapp:register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request, "email Taken")
                 return redirect('schoolapp:register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                return redirect('schoolapp:login')

        else:
            messages.info(request,"password not matching")
            return redirect('schoolapp:register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def order_confirmation(request):
    return render(request, 'order_confirmation.html')

