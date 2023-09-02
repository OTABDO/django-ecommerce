from django.urls import path, include
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.cart_summary, name="cart-summary"),
    path('add/', views.cart_add, name="cart-add"),
    path('update/', views.cart_update, name="cart-update"),
    path('delete', views.cart_delete, name="cart-delete"),
]
