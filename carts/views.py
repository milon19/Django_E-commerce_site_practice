from django.shortcuts import render
from .models import Cart


def Cart_Home(request):
    cart_obj = Cart.objects.new_or_get(request)
    return render(request, 'carts/cart-view.html', {})
