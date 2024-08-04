from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q

def home(request):
    search_form = SearchForm(request.GET)
    advanced_search_form = AdvancedSearchForm(request.GET)
    products = Product.objects.all()

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
    })

# View для деталей продукта
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            # Обработка данных формы
            product_name = form.cleaned_data.get('product_name')
            if product_name:
                # Выполнение поиска продуктов по названию
                products = Product.objects.filter(product_name__icontains=product_name)
                # Передача результатов поиска в контексте шаблона
                return render(request, 'search_results.html', {'products': products})
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form})

def onlinestore(request):
    search_form = AdvancedSearchForm(request.GET)
    if search_form.is_valid():
        product_name = search_form.cleaned_data.get('product_name')
        price = search_form.cleaned_data.get('price')
        category = search_form.cleaned_data.get('category')
        brand = search_form.cleaned_data.get('brand')
        color = search_form.cleaned_data.get('color')

        products = Product.objects.all()

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

        return render(request, 'search_results.html', {'products': products, 'search_form': search_form})

    return render(request, 'base.html', {
        'search_form': search_form,
    })