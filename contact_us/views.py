from django.shortcuts import render
from .forms import ContactForm
from django.http import JsonResponse, HttpResponse

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact',
        'content': ' Welcome to the contact page.',
        'form': contact_form,
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            data = {
                'message': 'Thank you for your submission'
            }
            return JsonResponse(data)

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    return render(request, 'contact_us/contact_view.html', context)
