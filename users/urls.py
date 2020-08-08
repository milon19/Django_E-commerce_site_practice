from django.urls import path
from .views import LoginView, LogoutView, RegisterView, guest_register_view

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/guest/', guest_register_view, name='guest_register'),

]

