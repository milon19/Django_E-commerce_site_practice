from django.urls import path
from .views import (CartHome, CartUpdate, CheckoutView)
from addresses.views import checkout_address_create_view

urlpatterns = [
    path('', CartHome, name='cart-home'),
    path('update/', CartUpdate, name='cart-update'),
    path('checkout/', CheckoutView, name='checkout'),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
]

