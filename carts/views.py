from django.shortcuts import render, redirect
from .models import Cart

from products.models import Product
from orders.models import Order


def CartHome(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    context = {
        'cart': cart_obj
    }
    return render(request, 'carts/cart-view.html', context)


def CartUpdate(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
            cart_obj, new_obj = Cart.objects.new_or_get(request)
            if product_obj in cart_obj.products.all():
                cart_obj.products.remove(product_obj)
            else:
                cart_obj.products.add(product_obj)
            request.session['cart_items'] = cart_obj.products.count()
        except Product.DoesNotExist:
            print('Massage to User: Product has gone')
            redirect('cart-home')
        # cart_obj.products.add(product_id)
    return redirect('cart-home')


def CheckoutView(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count()==0:
        return redirect('cart-home')
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    context = {
        'object': order_obj
    }
    return render(request, 'carts/checkout.html', context)
