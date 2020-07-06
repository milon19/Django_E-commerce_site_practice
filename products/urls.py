from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='products-list'),
    path('details/<str:pk>', ProductDetailView.as_view(), name='products-details'),
]

