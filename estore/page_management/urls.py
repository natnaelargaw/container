from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_page, name='about'),
    path('privacy/', views.privacy_page, name='privacy'),
    path('faq/', views.faqs_page, name='faq'),
    path('blog/', views.faqs_page, name='blog'),
    path('child/', views.home_page, name='child'),
]
