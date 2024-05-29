from django.urls import path
from . import views

urlpatterns = [
    path('', views.warehouseLandingPage, name='home'),
    path('v1/api/products', views.getAllProduct),
    path('v1/api/product/<int:id>', views.getProduct),
    path('v1/api/product/create', views.createProduct),
    path('v1/api/product/update/<int:id>', views.updateProduct),
    path('v1/api/product/delete/<int:id>', views.deleteProduct)
]