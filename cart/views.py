from django.shortcuts import render, redirect, reverse
from products.models import Feature


def view_cart(request):
    return render(request, 'cart.html')


def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart

    features = Feature.objects.all()
    return render(request, 'features.html', {'features': features})


def adjust_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
