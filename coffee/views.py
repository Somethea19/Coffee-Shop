from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee

# Create your views here.
def home(request):
    coffee = Coffee.objects.all()
    return render(request,'index.html',{'coffee': coffee})
def about(request):
    return render(request,'about.html')
def category(request):
    return render(request,'category.html')
def contact(request):
    return render(request,'contact.html')
def popular(request):
    return render(request,'popular.html')