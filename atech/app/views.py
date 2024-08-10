from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q

def home(request):
    search_form = SearchForm(request.GET)
    advanced_search_form = AdvancedSearchForm(request.GET)
    products = Product.objects.all()
    categories = Category.objects.all()

    if search_form.is_valid():
        product_name = search_form.cleaned_data.get('product_name')
        if product_name:
            products = products.filter(product_name__icontains=product_name)

    if advanced_search_form.is_valid():
        product_name = advanced_search_form.cleaned_data.get('product_name')
        price = advanced_search_form.cleaned_data.get('price')
        category = advanced_search_form.cleaned_data.get('category')
        brand = advanced_search_form.cleaned_data.get('brand')
        color = advanced_search_form.cleaned_data.get('color')

        if product_name:
            products = products.filter(product_name__icontains=product_name)
        if price:
            products = products.filter(price=price)
        if category:
            products = products.filter(category__in=category).distinct()
        if brand:
            products = products.filter(brand__in=brand).distinct()
        if color:
            products = products.filter(color__in=color).distinct()

    return render(request, 'base.html', {
        'search_form': search_form,
        'advanced_search_form': advanced_search_form,
        'products': products,
        'categories': categories,
    })

def category_view(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    search_form = SearchForm(request.GET)
    advanced_search_form = AdvancedSearchForm(request.GET)
    categories = Category.objects.all() 

    if search_form.is_valid():
        product_name = search_form.cleaned_data.get('product_name')
        if product_name:
            products = products.filter(product_name__icontains=product_name)

    if advanced_search_form.is_valid():
        product_name = advanced_search_form.cleaned_data.get('product_name')
        price = advanced_search_form.cleaned_data.get('price')
        brand = advanced_search_form.cleaned_data.get('brand')
        color = advanced_search_form.cleaned_data.get('color')

        if product_name:
            products = products.filter(product_name__icontains=product_name)
        if price:
            products = products.filter(price=price)
        if brand:
            products = products.filter(brand__in=brand).distinct()
        if color:
            products = products.filter(color__in=color).distinct()

    return render(request, 'category_view.html', {
        'category': category,
        'products': products,
        'search_form': search_form,
        'advanced_search_form': advanced_search_form,
        'categories': categories, 
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def search_view(request):
    form = SearchForm(request.GET)
    products = Product.objects.none()

    if form.is_valid():
        product_name = form.cleaned_data.get('product_name')
        if product_name:
            products = Product.objects.filter(product_name__icontains=product_name)

    return render(request, 'search_results.html', {
        'products': products,
        'form': form,
    })

def onlinestore(request):
    search_form = AdvancedSearchForm(request.GET)
    products = Product.objects.all()

    if search_form.is_valid():
        product_name = search_form.cleaned_data.get('product_name')
        price = search_form.cleaned_data.get('price')
        categories = search_form.cleaned_data.get('category')
        brands = search_form.cleaned_data.get('brand')
        colors = search_form.cleaned_data.get('color')

        if product_name:
            products = products.filter(product_name__icontains=product_name)

        if price:
            products = products.filter(price=price)

        if categories:
            products = products.filter(category__in=categories).distinct()

        if brands:
            products = products.filter(brand__in=brands).distinct()

        if colors:
            products = products.filter(color__in=colors).distinct()

    return render(request, 'search_results.html', {
        'products': products,
        'search_form': search_form,
    })