from django.shortcuts import render
from .forms import ContactForm

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact',
        'content': ' Welcome to the contact page.',
        'form': contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, 'contact_us/contact_view.html', context)
