from django.urls import path
from . import views

urlpatterns = [
    path("landing/", views.landing, name="landing"),
    path("products/", views.products, name="products"),
    path("signup/", views.signup, name="signup"),
    path("adminn/", views.adminn, name="admin"),
    path('create_products/', views.Createproducts.as_view(), name='Createproducts'),
    path('create_sell/', views.CreateSell.as_view(), name='create_sell'),
    path('addproducts/', views.addproducts, name='addproducts'),
    path('sell/', views.sell, name='sell'),
    path('create_cart/', views.Createcart.as_view(), name='Createcart'),
    path('check_user/', views.check_user, name='check_user'),
    path('cartnew/', views.cartnew, name='cartnew'),
    path('cart/', views.cart, name='cart'),
]