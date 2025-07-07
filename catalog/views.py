from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView

from catalog.models import Product


class HomeView(TemplateView):
    template_name = 'home.html'
    success_url = reverse_lazy('home')


class ContactsView(TemplateView):
    template_name = 'contacts.html'
    success_url = reverse_lazy('contacts')


class ProductPayView(TemplateView):
    template_name = 'pay.html'
    success_url = reverse_lazy('pay')


class ProductListView(ListView):
    model = Product
    template_name = 'product_catalog.html'
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_card.html'
    context_object_name = 'product'
