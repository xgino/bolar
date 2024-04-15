from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from Site.models import Site
from Service.models import Service
from Contact.models import Contact
from Contact.forms import ContactForm

def home(request):
    services = Service.objects.filter(active=True)
    form = ContactForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # Check if honeypot field is empty (indicating human submission)
        if not request.POST.get('honeypot'):
            form.save()
            messages.success(request, "Uw aanvraag is succesvol ingediend. We zullen binnen enkele werkdagen op uw bericht reageren.")
            redirect_url = reverse('Pages:home') + '#contact'
            return redirect(redirect_url)
        else:
            # Bot submission detected, reject it
            messages.error(request, "Bot submission detected. Please try again.")
    
    elif request.method == 'POST':
        for field, error_list in form.errors.as_data().items():
            for error in error_list:
                messages.error(request, f"{field.capitalize()}: {error}")

    return render(request, 'home.html', {
        'Site': Site.objects.first(), 
        'form': form, 
        'services': services})