from django.urls import path, include
from . import views

app_name = 'store'
urlpatterns = [
    # Store main page
    path('', views.store, name='store'),
    # Individual product
    path('product/<slug:product_slug>', views.product_info, name='product_detail'),
    # Individual category
    path('search/<slug:category_slug>', views.list_category, name='list-category')
]
