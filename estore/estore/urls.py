"""
URL configuration for estore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from page_management.views import home_page
from user_management.views import user_profile
urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', include('order_management.urls')),
    path('page/', include('page_management.urls')),
    path('product/', include('product_management.urls')),
    path('shopping/', include('shopping_cart.urls')),
    path('users/', include('user_management.urls')),
    path('', home_page, name="home" ),

    path("accounts/", include("django.contrib.auth.urls")),  # new
]
