from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Product
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator
class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

@method_decorator(login_required, name='dispatch')
class ProductCreate(CreateView):
    model = Product
    template_name = 'product_create.html'
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('product-list')
@method_decorator(login_required, name='dispatch')
class ProductUpdate(UpdateView):
    model = Product
    template_name = 'product_update.html'
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('product-list')
@method_decorator(login_required, name='dispatch')
class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product-list')
@method_decorator(login_required, name='dispatch')
class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
