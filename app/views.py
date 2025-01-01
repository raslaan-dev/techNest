from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
from .models import CartItem, Product

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

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('index')  # Redirect to home page
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')

    return render(request, 'app/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('register')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('index')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
            return redirect('register')

    return render(request, 'app/register.html')

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

def product_list(request):
    products = Product.objects.all()
    return render(request, 'app/products.html', {'products': products})

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        
        try:
            product = Product.objects.get(id=product_id)
            cart_item, created = CartItem.objects.get_or_create(
                user=request.user,
                product=product
            )
            
            if not created:
                cart_item.quantity += 1
                cart_item.save()
                
            cart_count = CartItem.objects.filter(user=request.user).count()
            return JsonResponse({'success': True, 'cart_count': cart_count})
        except Product.DoesNotExist:
            return JsonResponse({'success': False}, status=404)
    
    return JsonResponse({'success': False}, status=400)

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    cart_total = sum(item.total_price for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'cart_total': cart_total
    }
    return render(request, 'app/cart.html', context)

@login_required
def update_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('item_id')
        action = data.get('action')
        
        try:
            cart_item = CartItem.objects.get(id=item_id, user=request.user)
            
            if action == 'increase':
                cart_item.quantity += 1
            elif action == 'decrease':
                if cart_item.quantity > 1:
                    cart_item.quantity -= 1
                else:
                    cart_item.delete()
                    return JsonResponse({'success': True})
                    
            cart_item.save()
            return JsonResponse({'success': True})
        except CartItem.DoesNotExist:
            return JsonResponse({'success': False}, status=404)
    
    return JsonResponse({'success': False}, status=400)
