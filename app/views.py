from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def shop(request):
    return render(request, 'app/shop.html')

def sale(request):
    return render(request, 'app/sale.html')

def help(request):
    return render(request, 'app/help.html')
