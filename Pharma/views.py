from django.shortcuts import render

def homepage(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def shop(request):
    return render(request,'shop.html')

def contact(request):
    return render(request,'contact.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def thankyou(request):
    return render(request,'thankyou.html')
