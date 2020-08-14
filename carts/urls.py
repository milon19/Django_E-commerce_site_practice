from django.urls import path
from .views import (CartHome, CartUpdate, CheckoutView, checkout_done, cart_detail_api_view)
from addresses.views import checkout_address_create_view, checkout_address_reuse_view

urlpatterns = [
    path('', CartHome, name='cart-home'),
    path('api/cart/', cart_detail_api_view, name='api-cart'),
    path('update/', CartUpdate, name='cart-update'),
    path('checkout/', CheckoutView, name='checkout'),
    path('checkout/success', checkout_done, name='checkout-success'),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
]

