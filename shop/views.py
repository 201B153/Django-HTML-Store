from .models import Product
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    products = Product.objects.all()
    print(products[0].product_desc)
    context = {"products": products, }
    return render(request, "shop/index.html", context)
