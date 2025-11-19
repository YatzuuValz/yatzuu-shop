from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForms
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import datetime
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.utils.html import strip_tags

import json
import requests

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all().order_by("-created_at")
    else:
        product_list = Product.objects.filter(user=request.user).order_by("-created_at")

    context = {
        'npm' : '2406415936',
        'name': 'Yahya Muhandar Fathana',
        'class': 'PBP F',
        'ProjectName': 'Yatzuu Shop',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = strip_tags(data.get("name", ""))  # Strip HTML tags
        price  = data.get("price", "")  # Strip HTML tags
        ongkir  = data.get("ongkir", "")  # Strip HTML tags
        description   = strip_tags(data.get("description", ""))  # Strip HTML tags
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)
        user = request.user
        
        new_product = Product(
            name=name,
            price=price,
            ongkir=ongkir,
            description=description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            user=user,
        )
        new_product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def create_product(request):
    form = ProductForms(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'ongkir': product.ongkir,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'rating': product.rating,
            'item_views': product.item_views,
            'is_featured': product.is_featured,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_recommended' : product.is_recommended,
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
   
def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'ongkir': product.ongkir,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'rating': product.rating,
            'item_views': product.item_views,
            'is_featured': product.is_featured,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_recommended' : product.is_recommended,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   
   
def edit_product(request, id):
    products = get_object_or_404(Product, pk=id)
    form = ProductForms(request.POST or None, instance=products)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

@csrf_exempt
def delete_product(request, id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return JsonResponse({"success": True, "message": "Product deleted successfully!"})
    else:
        return JsonResponse({"success": False, "message": "Invalid request method."}, status=405)

...
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("title")) # strip HTML tags!
    name = request.POST.get("name")
    price = request.POST.get("price")
    ongkir = request.POST.get("ongkir")
    description  = strip_tags(request.POST.get("content"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    product_product = Product(
        name=name, 
        price=price, 
        ongkir=ongkir, 
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    product_product.save()

    return HttpResponse(b"CREATED", status=201)

from django.contrib.auth.models import User
@csrf_exempt
def ajax_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            return JsonResponse({"success": False, "message": "Passwords do not match."}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"success": False, "message": "Username already exists."}, status=400)

        user = User.objects.create_user(username=username, password=password1)
        user.save()
        return JsonResponse({"success": True, "message": "Account created successfully!"})

    return JsonResponse({"success": False, "message": "Invalid request method."}, status=405)


@csrf_exempt
def ajax_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"success": True, "message": "Login successful!"})
        else:
            return JsonResponse({"success": False, "message": "Invalid username or password."}, status=400)

    return JsonResponse({"success": False, "message": "Invalid request method."}, status=405)
