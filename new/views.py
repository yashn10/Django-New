from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as out
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password
from .models import Category, Product, Signup, Contact

# Create your views here.

def home(request):
    category = Category.objects.all()
    # cat_id = request.GET.get('category')

    # if cat_id:
    #     cat = get_object_or_404(Category, id=cat_id)
    #     products = Product.objects.filter(category=cat)
    # else:
    products = Product.objects.all()

    context = {
        "category": category,
        "products": products,
    }

    return render(request, 'home.html', context)


def about(request):
    return render(request, 'detail.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        user = Contact(name=name, email=email, subject=subject, message=message)
        user.save()
        return redirect('home')

    return render(request, 'contact.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request, id):
    product = Product.objects.filter(id=id).first

    context = {
        "product": product
    }

    return render(request, 'checkout.html', context)


def search(request):
    query = request.GET['name']
    products = Product.objects.filter(name__icontains=query)

    context = {
        "products": products
    }
    return render(request, 'search.html', context)


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        
        # Simple form validation
        if not name or not email or not contact or not password:
            messages.error(request, 'All fields are required')
            return redirect('signup')
        
        # Check if the email is unique
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('signup')
        
        try:
            # Hash the password
            hashed_password = make_password(password)
            
            # Create the user
            user = User.objects.create(
                username=email,  # Use email as the username
                email=email,
                password=hashed_password
            )
            user.first_name = name  # Set the name
            user.save()

            messages.success(request, 'User registered successfully')
            return redirect('login')
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e):
                messages.error(request, 'Email already registered')
            else:
                messages.error(request, 'Database error')
            print(f'IntegrityError: {e}')
        except Exception as e:
            messages.error(request, 'Error registering user')
            print(f'Exception: {e}')
    
    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfull')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')

    return render(request, 'signin.html')


def logout(request):
    
    out(request)
    messages.success(request, "Logout Successfully")
    return redirect('login')


def shop(request):

    category = Category.objects.all()
    cat_id = request.GET.get('category')

    if cat_id:
        cat = get_object_or_404(Category, id=cat_id)
        products = Product.objects.filter(category=cat)
    else:
        products = Product.objects.all()

    context = {
        "category": category,
        "products": products
    }
        
    return render(request, 'shop.html', context)
    

def detail(request, id):
    product = get_object_or_404(Product, id=id)

    context = {
        'product': product
    }

    return render(request, 'detail.html', context)
