from django.shortcuts import render, HttpResponse, redirect
from .models import student

# Create your views here.
def index(request):
    if request.method=="POST":
        name= request.POST['name']
        email= request.POST['email']
        address= request.POST['address']
        student.objects.create(name=name, email=email, address=address)
        return redirect("/")
    else:
        data= {
            'studentsData': student.objects.all()
        }
        
    return render(request,'index.html',data)

def about(request):
    return render(request,'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')
