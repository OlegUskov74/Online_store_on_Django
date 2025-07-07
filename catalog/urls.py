from django.urls import path, include
from catalog.apps import CatalogConfig
from .views import HomeView, ContactsView, ProductPayView, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path("product_card/<int:pk>/", ProductDetailView.as_view(), name="product_card"),
    path('product_catalog/', ProductListView.as_view(), name='product_catalog'),
    path('pay/', ProductPayView.as_view(), name='pay'),
]
