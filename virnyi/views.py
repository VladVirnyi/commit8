from django.shortcuts import render, get_object_or_404
from .models import MenuCategory, MenuItem


def home(request):
    return render(request, 'home.html')


def page1(request):
    return render(request, 'page1.html')


def page2(request):
    return render(request, 'page2.html')


def page3(request):
    return render(request, 'page3.html')


def page4(request):
    return render(request, 'page4.html')


def category_list(request):
    categories = MenuCategory.objects.filter(is_available=True)
    return render(request, 'category_list.html', {
        'categories': categories
    })


def category_detail(request, category_id):
    category = get_object_or_404(MenuCategory, id=category_id)
    products = MenuItem.objects.filter(category=category, is_available=True)
    return render(request, 'category_detail.html', {
        'category': category,
        'products': products
    })



def product_detail(request, product_id):
    product = get_object_or_404(MenuItem, id=product_id)
    return render(request, 'product_detail.html', {
        'product': product
    })



