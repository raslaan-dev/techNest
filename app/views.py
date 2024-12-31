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

def login(request):
    return render(request, 'app/login.html')

def cart(request):
    return render(request, 'app/cart.html')

def terms(request):
    return render(request, 'app/terms.html')

def accessibility(request):
    return render(request, 'app/accessibility.html')

def shipping(request):
    return render(request, 'app/shipping.html')

def privacy(request):
    return render(request, 'app/privacy.html')

def refund(request):
    return render(request, 'app/refund.html')
