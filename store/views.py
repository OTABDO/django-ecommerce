from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def store(request: WSGIRequest) -> HttpResponse:
    all_products = Product.objects.all()
    context = {'all_products': all_products}
    return render(request, template_name='store/store.html', context=context)


def categories(request: WSGIRequest) -> dict:
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}


def list_category(request: WSGIRequest, category_slug=None) -> HttpResponse:
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {'category': category, 'products': products}
    return render(request, template_name='store/list_category.html', context=context)


def product_info(request: WSGIRequest, product_slug: Product) -> HttpResponse:
    product = get_object_or_404(Product, slug=product_slug)
    context = {'product': product}
    return render(request, template_name='store/product_info.html', context=context)
