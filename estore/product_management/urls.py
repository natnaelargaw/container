from django.contrib import admin
from django.urls import path
from . import views
from .views import ProductList, ProductCreate, ProductUpdate, ProductDelete, ProductDetail
urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('create/', ProductCreate.as_view(), name='product-create'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='product-update'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='product-delete'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]
