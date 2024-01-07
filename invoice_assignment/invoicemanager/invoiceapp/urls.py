# invoiceapp/urls.py
from django.urls import path
from .views import invoice_list, invoice_detail

urlpatterns = [
    path('invoices/', invoice_list, name='invoice-list'),
    path('invoices/<int:pk>/', invoice_detail, name='invoice-detail'),
]
