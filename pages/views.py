from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User, Babie, Sitter, Pickup

# Create your views here.
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
        return render(request,'404.html', {"title": "Admin Home"})

def login(request):
    return render(request,'login.html', {"title": "Login"})

def about(request):
    return render(request,'about.html', {"title": "About"})

def contact(request):
    return render(request,'contact.html', {"title": "Contact"})

def sitter(request):
    if request.method == "POST":
        blog_title = request.POST['blog_title']
        blog_content = request.POST['blog_content']
        blog_tag = request.POST['blog_tag']
        blog_image = request.POST['blog_image']
        blog_date = request.POST['blog_date']
        bl = MyBlogs(title=blog_title, content=blog_content, tag=blog_tag, image=blog_image, date_posted=blog_date)
        bl.save()
    return render(request,'sitter.html', {"title": "Sitter"})

def sitters(request):
    return render(request,'sitters.html', {"title": "Sitters"})

def babies(request):
    return render(request,'babies.html', {"title": "Babies"})

def shop(request):
    return render(request,'shop.html', {"title": "Shop"})
