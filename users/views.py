from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegistrationForm, GuestForm
from django.utils.http import is_safe_url
from django.shortcuts import redirect, render
from .models import GuestEmail


class LoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    success_message = 'You are successfully logged in'

    def dispatch(self, request, *args, **kwargs):
        try:
            del request.session['guest_email_id']
        except:
            pass
        return super().dispatch(request, *args, **kwargs)


class LogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = 'home'


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'
    success_message = 'Registration is completed. Please Login in here'


def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        'form': form,
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    if form.is_valid():
        email = form.cleaned_data.get('email')
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('users/register.html')
    return render(request, 'users/register.html', context)
