from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
from .models import CartItem, Product, Category, Order
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.db import models

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    selected_categories = request.GET.getlist('category')  # Get selected categories

    # Search filter
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # Category filter
    if selected_categories:
        products = products.filter(category_id__in=selected_categories)

    # Price range filter
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Sorting
    sort = request.GET.get('sort')
    if sort:
        if sort == 'price_asc':
            products = products.order_by('price')
        elif sort == 'price_desc':
            products = products.order_by('-price')
        elif sort == 'name_asc':
            products = products.order_by('name')
        elif sort == 'name_desc':
            products = products.order_by('-name')

    context = {
        'products': products,
        'categories': categories,
        'selected_categories': selected_categories,  # Pass to template
    }
    return render(request, 'app/shop.html', context)

def sale(request):
    # Update this query to use sale_price instead of original_price
    sale_products = Product.objects.filter(sale_price__isnull=False).order_by('name')
    return render(request, 'app/sale.html', {'products': sale_products})

def help(request):
    return render(request, 'app/help.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Get the next parameter or default to home
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
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

@require_POST
def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    try:
        product = Product.objects.get(id=product_id)
        # Add to cart logic here (you'll need to implement this based on your cart model)
        # For example:
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
            
        return JsonResponse({'success': True})
    except Product.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Product not found'})

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

def cart_sidepanel(request):
    cart_items = CartItem.objects.filter(user=request.user) if request.user.is_authenticated else []
    cart_total = sum(item.product.price * item.quantity for item in cart_items)
    
    return render(request, 'app/cart_sidepanel.html', {
        'cart_items': cart_items,
        'cart_total': cart_total,
    })

@staff_member_required
def product_management(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')
        
        Product.objects.create(
            name=name,
            description=description,
            price=price,
            stock=stock,
            image=image
        )
        return redirect('product_management')
    
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'app/product_management.html', {'products': products})

@staff_member_required
def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        return redirect('product_management')
    
    return render(request, 'app/edit_product.html', {'product': product})

@staff_member_required
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('product_management')

@login_required(login_url='login')
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    subtotal = sum(item.total_price for item in cart_items)
    total = subtotal  # Add shipping calculation if needed

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'total': total,
    }
    return render(request, 'app/checkout.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'app/product_detail.html', {'product': product})

def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user) if request.user.is_authenticated else []
    cart_total = sum(item.total_price for item in cart_items)
    
    return render(request, 'app/cart.html', {
        'cart_items': cart_items,
        'cart_total': cart_total,
    })

@require_POST
def remove_from_cart(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id, user=request.user)
        cart_item.delete()
        
        # Calculate new cart total
        cart_items = CartItem.objects.filter(user=request.user)
        cart_total = sum(item.total_price for item in cart_items)
        
        return JsonResponse({
            'success': True,
            'cart_total': cart_total,
            'is_empty': not cart_items.exists()
        })
    except CartItem.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Item not found'
        })

def profile_view(request):
    return render(request, 'app/profile.html')

@login_required(login_url='login')
def payment(request):
    if request.method == 'POST':
        # Get cart items and totals
        cart_items = CartItem.objects.filter(user=request.user)
        subtotal = sum(item.total_price for item in cart_items)
        total = subtotal  # Add shipping calculation if needed

        context = {
            'cart_items': cart_items,
            'subtotal': subtotal,
            'total': total,
        }
        return render(request, 'app/payment.html', context)
    return redirect('checkout')

@login_required(login_url='login')
def process_payment(request):
    if request.method == 'POST':
        # Here you would integrate with your payment processor
        # For now, we'll just simulate a successful payment
        cart_items = CartItem.objects.filter(user=request.user)
        
        # Create order
        order = Order.objects.create(
            user=request.user,
            total_amount=sum(item.total_price for item in cart_items)
        )
        
        # Clear cart
        cart_items.delete()
        
        messages.success(request, 'Payment successful! Your order has been placed.')
        return redirect('order_confirmation')
    
    return redirect('checkout')

@login_required(login_url='login')
def order_confirmation(request):
    # Get the most recent order for the user
    order = Order.objects.filter(user=request.user).latest('created_at')
    return render(request, 'app/order_confirmation.html', {'order': order})
