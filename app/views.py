from django.shortcuts import render,redirect
from .models import *
from django.conf import settings

# Create your views here.

def home(request):
    try:
        usr = user.objects.all()
        return render(request, "app/home.html",{'usr' : usr})
    except:
        pass

def add_user_page(request):
    try:
        return render(request, "app/Add-user.html")
    except:
        return redirect("home")

def Edit_user_page(request,pk):
    try:
        getuser = user.objects.get(id=pk)
        return render(request, "app/Edit-user.html",{'data':getuser})
    except:
        return redirect("home")

def add_user(request):
    try:
        if request.method == "POST":
            nm = request.POST['name']
            usrnm = request.POST['username']
            em = request.POST['email']
            img = request.FILES['image']

            usr = user.objects.create(
                name = nm,
                username = usrnm,
                email = em,
                Image = img,
            )
            return redirect('home')
        else:
            return redirect('home')
    except:
        return redirect("home")

def deletuser(request,pk):
    try:
        getuser = user.objects.get(id=pk)
        getuser.delete()
        return redirect('home')
    except:
        return redirect("home")

def updateusr(request,pk):
    try:
        getuser = user.objects.get(id=pk)
        getuser.name = request.POST['name'] if request.POST['name'] else getuser.name
        getuser.username = request.POST['username'] if request.POST['username'] else getuser.username
        getuser.email = request.POST['email'] if request.POST['email'] else getuser.email
        try:
            getuser.Image = request.FILES['image'] if request.FILES['image'] else getuser.Image
        except:
            pass
        getuser.save()
        return redirect('home')
    except:
        return redirect("home")
