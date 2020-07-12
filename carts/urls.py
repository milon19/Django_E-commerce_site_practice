from django.urls import path
from .views import Cart_Home

urlpatterns = [
    path('', Cart_Home, name='cart-home'),
]

