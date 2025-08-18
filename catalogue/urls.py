from django.urls import path
from .views import list_products, product_detail  

urlpatterns = [
    path("products/", list_products, name="list_products"),
    path("products/<int:id>/", product_detail, name="product_detail"), 
]
