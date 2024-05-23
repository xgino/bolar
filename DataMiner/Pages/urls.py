from django.urls import path
from . import views

app_name='Pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('marketing/', views.marketing, name='marketing'),
    path('marketing/Ontgrendel Lokale Bedrijfsinzichten/', views.gmap_scraper, name='gmap_scraper'),
    path('marketing/Verhoog Uw Bereik met Lokale Bedrijfsemail lijst/', views.gmap_email_scraper, name='gmap_email_scraper'),
    path('marketing/Verhoog Uw Website Verkeer en Google Ranking met Onze SEO Boost/', views.SEO_boost, name='SEO_boost'),
    path('andere service/', views.other_scrapers, name='other_scrapers'),
    path('andere service/Lijst van Talentvolle Bijna Afgestudeerde Studenten/', views.Linkedin_student, name='Linkedin_student'),
    path('andere service/Ontdek de Kracht van YouTube-video Boost/', views.YouTube_Boost, name='YouTube_Boost'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
]