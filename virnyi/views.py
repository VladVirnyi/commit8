from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuCategory, MenuItem
from .forms import OrderForm



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


def create_order(request, product_id):
    product = get_object_or_404(MenuItem, id=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product

            temperature = form.cleaned_data.get('temperature')
            size = form.cleaned_data.get('size')
            quantity = form.cleaned_data.get('quantity')

            notes = f"Температура: {dict(form.fields['temperature'].choices)[temperature]}\n"
            notes += f"Розмір: {dict(form.fields['size'].choices)[size]}\n"
            notes += f"Кількість: {quantity}\n"
            if order.notes:
                notes += f"\nДодаткові примітки: {order.notes}"
            order.notes = notes

            order.save()
            return redirect('order_success')
    else:
        initial_data = {}
        if product.temperature != 'both':
            initial_data['temperature'] = product.temperature
        form = OrderForm(initial=initial_data)

    return render(request, 'product_detail.html', {
        'form': form,
        'product': product
    })


def order_success(request):
    return render(request, 'order_success.html', {
        'message': 'Дякуємо за ваше замовлення! Ми зв\'яжемося з вами найближчим часом.'
    })

