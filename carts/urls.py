from django.urls import path
from .views import (CartHome, CartUpdate, CheckoutView)

urlpatterns = [
    path('', CartHome, name='cart-home'),
    path('update/', CartUpdate, name='cart-update'),
    path('checkout/', CheckoutView, name='checkout'),
]

