from django.shortcuts import render, redirect
from .models import Member
from django.db.models import Q
from django.contrib.auth.models import User, auth
from django.contrib import messages





# Create your views here.
def members(request):
    members = Member.objects.all()
    context = {"members": members}
    return render(request, "members.html", context)


def main(request):
    return render(request, "main.html")


def details(request, slug):
    member = Member.objects.get(slug=slug)
    context = {"member": member}
    return render(request, "details.html", context)


def testing(request):
    mydata = Member.objects.all().order_by('fname').values()
    context = {
        "mymembers": mydata,
    }
    return render(request, "test.html", context)


def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name already used')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password mismatched')
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'credentials invalid')
            return redirect('login')
    else:
        return render(request,'login.html')
    
    
def logout(request):
    auth.logout(request)
    return redirect('/')