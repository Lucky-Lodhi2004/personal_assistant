from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, 'core/Login.html')

def register(request):
    return render(request, 'core/Register.html')

def about(request):
    return render(request, 'core/About.html')

def dashboard(request):
    return render(request, 'core/Dashboard.html')
