from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')

def privacy_page(request):
    return render(request, 'privacy.html')

def faqs_page(request):
    return render(request, 'faq.html')

def blog_page(request):
    return render(request, 'blog.html')
