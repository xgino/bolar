import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import FileResponse

from Site.models import Site
from Service.models import Service, ServiceCategory
from Contact.forms import EmailForm
from Contact.models import Quote, DownloadRecord
from Contact.forms import QuoteForm

def home(request):

    return render(request, 'home.html', {
        'Site': Site.objects.first(), 
        })


def about(request):
    return render(request, 'about.html', {
        'Site': Site.objects.first(), 
        })


def marketing(request):
    return render(request, 'marketing.html', {
        'Site': Site.objects.first(), 
        })

def gmap_scraper(request):
    service_category = ServiceCategory.objects.get(name='Ontgrendel Lokale Bedrijfsinzichten')
    services = service_category.services.filter(active=True).order_by('quantity')

    quote_form = QuoteForm(request.POST or None)
    if request.method == 'POST':
        if quote_form.is_valid():
            # Check if honeypot field is empty (indicating human submission)
            if not request.POST.get('honeypot'):
                quote_form.save()
                messages.success(request, "Uw aanvraag is succesvol ingediend. We zullen binnen enkele werkdagen op uw bericht reageren.")
                redirect_url = reverse('Pages:gmap_scraper') + '#form_status'
                return redirect(redirect_url)
            else:
                # Bot submission detected, reject it
                messages.error(request, "Bot submission detected. Please try again.")
    
        else:
            for field, error_list in quote_form.errors.as_data().items():
                for error in error_list:
                    messages.error(request, f"{field.capitalize()}: {error}")


    email_form = EmailForm(request.POST or None)
    if request.method == 'POST':
        if 'download_file' in request.POST and email_form.is_valid():
            email = email_form.cleaned_data['email']
            file_name = 'gmap_scraper.csv'
            file_path = os.path.join('Data', file_name)

            # Create a DownloadRecord
            DownloadRecord.objects.create(email=email, file_name=file_name, file_path=file_path)

            # Serve the file
            response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
            return response


    return render(request, 'marketing/gmap_scraper.html', {
        'Site': Site.objects.first(), 
        'services': services,
        'email_form': email_form,
        })


def gmap_email_scraper(request):
    service_category = ServiceCategory.objects.get(name='Verhoog Uw Bereik met Lokale Bedrijfsemail lijst')
    services = service_category.services.filter(active=True).order_by('quantity')

    quote_form = QuoteForm(request.POST or None)
    if request.method == 'POST':
        if quote_form.is_valid():
            # Check if honeypot field is empty (indicating human submission)
            if not request.POST.get('honeypot'):
                quote_form.save()
                messages.success(request, "Uw aanvraag is succesvol ingediend. We zullen binnen enkele werkdagen op uw bericht reageren.")
                redirect_url = reverse('Pages:gmap_email_scraper') + '#form_status'
                return redirect(redirect_url)
            else:
                # Bot submission detected, reject it
                messages.error(request, "Bot submission detected. Please try again.")
    
        else:
            for field, error_list in quote_form.errors.as_data().items():
                for error in error_list:
                    messages.error(request, f"{field.capitalize()}: {error}")


    email_form = EmailForm(request.POST or None)
    if request.method == 'POST':
        if 'download_file' in request.POST and email_form.is_valid():
            email = email_form.cleaned_data['email']
            file_name = 'gmap_email_scraper.csv'
            file_path = os.path.join('Data', file_name)

            # Create a DownloadRecord
            DownloadRecord.objects.create(email=email, file_name=file_name, file_path=file_path)

            # Serve the file
            response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
            return response


    return render(request, 'marketing/gmap_email_scraper.html', {
        'Site': Site.objects.first(), 
        'services': services,
        'email_form': email_form,
        })


def SEO_boost(request):
    service_category = ServiceCategory.objects.get(name='SEO Boost')
    services = service_category.services.filter(active=True).order_by('quantity')

    quote_form = QuoteForm(request.POST or None)
    if request.method == 'POST':
        if quote_form.is_valid():
            # Check if honeypot field is empty (indicating human submission)
            if not request.POST.get('honeypot'):
                quote_form.save()
                messages.success(request, "Uw aanvraag is succesvol ingediend. We zullen binnen enkele werkdagen op uw bericht reageren.")
                redirect_url = reverse('Pages:SEO_boost') + '#form_status'
                return redirect(redirect_url)
            else:
                # Bot submission detected, reject it
                messages.error(request, "Bot submission detected. Please try again.")
        else:
            # Form is invalid, display error messages
            for field, error_list in quote_form.errors.as_data().items():
                for error in error_list:
                    messages.error(request, f"{field.capitalize()}: {error}")


    email_form = EmailForm(request.POST or None)
    if request.method == 'POST':
        if 'download_file' in request.POST and email_form.is_valid():
            email = email_form.cleaned_data['email']
            file_name = 'SEO_boost.csv'
            file_path = os.path.join('Data', file_name)

            # Create a DownloadRecord
            DownloadRecord.objects.create(email=email, file_name=file_name, file_path=file_path)

            # Serve the file
            response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
            return response


    return render(request, 'marketing/SEO_boost.html', {
        'Site': Site.objects.first(), 
        'services': services,
        'email_form': email_form,
        })




def other_scrapers(request):
    return render(request, 'other_scrapers.html', {
        'Site': Site.objects.first(), 
        })


def Linkedin_student(request):
    service_category = ServiceCategory.objects.get(name='Linkedin Student')
    services = service_category.services.filter(active=True).order_by('quantity')

    quote_form = QuoteForm(request.POST or None)
    if request.method == 'POST':
        if quote_form.is_valid():
            # Check if honeypot field is empty (indicating human submission)
            if not request.POST.get('honeypot'):
                quote_form.save()
                messages.success(request, "Uw aanvraag is succesvol ingediend. We zullen binnen enkele werkdagen op uw bericht reageren.")
                redirect_url = reverse('Pages:Linkedin_student') + '#form_status'
                return redirect(redirect_url)
            else:
                # Bot submission detected, reject it
                messages.error(request, "Bot submission detected. Please try again.")
        else:
            # Form is invalid, display error messages
            for field, error_list in quote_form.errors.as_data().items():
                for error in error_list:
                    messages.error(request, f"{field.capitalize()}: {error}")


    email_form = EmailForm(request.POST or None)
    if request.method == 'POST':
        if 'download_file' in request.POST and email_form.is_valid():
            email = email_form.cleaned_data['email']
            file_name = 'Linkedin_Student.csv'
            file_path = os.path.join('Data', file_name)

            # Create a DownloadRecord
            DownloadRecord.objects.create(email=email, file_name=file_name, file_path=file_path)

            # Serve the file
            response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
            return response


    return render(request, 'andere_service/Linkedin_student.html', {
        'Site': Site.objects.first(), 
        'services': services,
        'email_form': email_form,
        })



def YouTube_Boost(request):
    service_category = ServiceCategory.objects.get(name='YouTube Boost')
    services = service_category.services.filter(active=True).order_by('quantity')

    quote_form = QuoteForm(request.POST or None)
    if request.method == 'POST':
        if quote_form.is_valid():
            # Check if honeypot field is empty (indicating human submission)
            if not request.POST.get('honeypot'):
                quote_form.save()
                messages.success(request, "Uw aanvraag is succesvol ingediend. We zullen binnen enkele werkdagen op uw bericht reageren.")
                redirect_url = reverse('Pages:YouTube_Boost') + '#form_status'
                return redirect(redirect_url)
            else:
                # Bot submission detected, reject it
                messages.error(request, "Bot submission detected. Please try again.")
        else:
            # Form is invalid, display error messages
            for field, error_list in quote_form.errors.as_data().items():
                for error in error_list:
                    messages.error(request, f"{field.capitalize()}: {error}")


    email_form = EmailForm(request.POST or None)
    if request.method == 'POST':
        if 'download_file' in request.POST and email_form.is_valid():
            email = email_form.cleaned_data['email']
            file_name = 'Youtube_boost.csv'
            file_path = os.path.join('Data', file_name)

            # Create a DownloadRecord
            DownloadRecord.objects.create(email=email, file_name=file_name, file_path=file_path)

            # Serve the file
            response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
            return response


    return render(request, 'andere_service/YouTube_Boost.html', {
        'Site': Site.objects.first(), 
        'services': services,
        'email_form': email_form,
        })






def faq(request):
    return render(request, 'faq.html', {
        'Site': Site.objects.first(), 
        })


def contact(request):
    return render(request, 'contact.html', {
        'Site': Site.objects.first(), 
        })