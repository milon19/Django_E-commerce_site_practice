from django.urls import path
from .views import (CartHome, CartUpdate)

urlpatterns = [
    path('', CartHome, name='cart-home'),
    path('update/', CartUpdate, name='cart-update'),
]

