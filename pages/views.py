from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User, Babie, Sitter, Pickup
import random

# Create your views here.
def baby(request):
    if request.method == "POST":
        cname = request.POST['cname']
        nop = request.POST['nop']
        comm = request.POST['comm']
        pick = Pickup(baby=cname, name_of_person=nop, comment=comm)
        pick.save()
        return render(request,'index.html')
    keep = Babie.objects.all()
    return render(request,'baby.html', {"title": "Babies", "babys" : keep})

def home(request):
    if request.method == "POST":
        uname = request.POST['uname']
        val = User.objects.filter(username=uname)
        if val.exists():
            for obj in val:
                if obj.password == request.POST['pword']:
                    return render(request,'index.html')
                else:
                    return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request,'404.html', {"title": "Page Not Found"})

def login(request):
    return render(request,'login.html', {"title": "Login"})

def about(request):
    return render(request,'about.html', {"title": "About"})

def contact(request):
    return render(request,'contact.html', {"title": "Contact"})

def sitter(request):
    if request.method == "POST":
        nom = request.POST['name']
        ou = request.POST['location']
        birth = request.POST['dob']
        sex = request.POST['gender']
        nex = request.POST['nok']
        nation = request.POST['nin']
        rec = request.POST['recommender']
        relig = request.POST['religion']
        edu = request.POST['loe']
        sin = request.POST['sin']
        tel = request.POST['tel']
        sit = Sitter(name=nom, location=ou, date_of_Birth=birth, gender=sex, next_of_kin=nex, nin=nation,recomender_name=rec, religion=relig, level_of_education=edu, sitter_number=sin, contact=tel)
        sit.save()
    return render(request,'sitter.html', {"title": "Sitter"})

def sitters(request):
    keeper = Sitter.objects.all()
    return render(request,'sitters.html', {"title" : "Sitters", "sits" : keeper})

def babies(request):
    if request.method == "POST":
        nom = request.POST['name']
        ou = request.POST['location']
        brought = request.POST['brought']
        sex = request.POST['gender']
        pare = request.POST['parent']
        fe = request.POST['fee']
        periodt = request.POST['period']
        baen = request.POST['bin']
        ag = request.POST['age']
        available = Sitter.objects.filter(on_duty=True)
        for sittr in available:
            on = []
            on.append(sittr.name)
            y = random.randrange(len(on))
            sin = on[y]
        babe = Babie(name=nom, location=ou, brought_by=brought, gender=sex, parent_name=pare, fee=fe,period_of_stay=periodt, baby_number=baen, age=ag, sitter=sin)
        babe.save()
    return render(request,'babies.html', {"title": "Register Baby"})

def shop(request):
    return render(request,'shop.html', {"title": "Shop"})

def delete(request, baby_id):
    Babie.objects.filter(id=baby_id).delete()
    return HttpResponseRedirect(reverse('baby'))

def edit(request, baby_id):
    Babie.objects.filter(id=baby_id).delete()
    return HttpResponseRedirect(reverse('baby'))

def erase(request, sitter_id):
    Sitter.objects.filter(id=sitter_id).delete()
    return HttpResponseRedirect(reverse('sitters'))

def update(request, sitter_id):
    Sitter.objects.filter(id=sitter_id).delete()
    return HttpResponseRedirect(reverse('sitters'))