from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def forms(request):
    if request.method == "POST":
        query = Login.objects.create(
            name=request.POST['name'], email=request.POST['email'], password=request.POST['password'],profile_pic=request.FILES['file1'])
        query.save()
        return view(request)
    return render(request, 'form.html')


def view(request):
    query = Login.objects.all()
    return render(request, 'view.html', {"query": query})


def update(request, email):
    query = Login.objects.filter(email=email)
    if request.method == "POST":
        Login.objects.filter(email=email).update(
            name=request.POST['name'], password=request.POST['password'])
        return index(request)
    return render(request, 'update.html', {"query": query})


def delete(request, email):
    Login.objects.filter(email=email).delete()

    return index(request)
