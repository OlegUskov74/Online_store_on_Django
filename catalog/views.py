from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:product_catalog')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        """ Перенаправление на страницу созданного блога. """
        return reverse("catalog:product_card", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_catalog')