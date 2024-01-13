from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name='store'),
    path('cart/',views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add/<int:product_id>/', views.add, name='add'),
    path('remove/<int:product_id>/', views.remove, name='remove'),
]