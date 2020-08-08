from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegistrationForm


class LoginView(SuccessMessageMixin, LoginView):
    redirect_authenticated_user = True
    template_name = 'users/login.html'
    success_message = 'You are successfully logged in'


class LogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = 'home'


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'
    success_message = 'Registration is completed. Please Login in here'
