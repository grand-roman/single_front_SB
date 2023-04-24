from django.urls import path
from api import views

urlpatterns = [
    path('banners/', views.banners),
    path('categories/', views.categories),
    path('catalog/', views.catalog),
    path('products/popular/', views.productsPopular),
    path('products/limited/', views.productsLimited),
    path('sales/', views.sales),
    path('basket/', views.basket),
    path('orders/', views.orders),
    path('sign-in/', views.signIn),
    path('sign-out/', views.signOut),
]
