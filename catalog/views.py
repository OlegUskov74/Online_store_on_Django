from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def product_card(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {"product": product}
    return render(request, "product_card.html", context=context)


def product_catalog(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'product_catalog.html', context=context)

def pay(request):
    return render(request, "pay.html")