from django.shortcuts import render

def index(request):
    return render(request,'first/index.html')
    return render(request,'registration/login.html')
    