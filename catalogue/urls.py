from django.urls import path
from .views import list_products, product_detail
from .views import create_product
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('products/', list_products, name='list_products'),
    path('products/<int:id>/',product_detail, name='product_details' ),
    path("products/create/", create_product, name='create_product'),
    path('products/login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('products/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
