from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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

        user = Signup(name=name, email=email, contact=contact, password=password)
        
        try:
            user = Signup.objects.create(name=name, email=email, contact=contact, password=password)
            messages.success(request, 'User registered successfully')
            return redirect('login')
        except Exception as e:
            messages.error(request, 'Error registering user')
            print(e)


    return render(request, 'signup.html')


def signin(request):
    return render(request, 'signin.html')


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
