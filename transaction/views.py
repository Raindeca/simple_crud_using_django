from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Order

# Create generic template
class IndexView(generic.ListView):
    template_name = 'transaction/index.html'
    context_object_name = 'all_transactions'

    # fetch all data in order with addition related data to costumer and book
    def get_queryset(self):
        return Order.objects.all().select_related('costumer').select_related('book')

# read detail data in transaction
class DetailView(generic.DetailView):
    model = Order
    template_name = 'transaction/detail.html'
    
# add a new transaction
class TransactionCreate(CreateView):
    model = Order
    fields = [
        'costumer',
        'book',
        'payment',
        'total_price',
    ]

# Update a transaction data
class TransactionUpdate(UpdateView):
    model = Order
    fields = [
        'costumer',
        'book',
        'payment',
        'total_price',
    ]

# delete a transaction data
class TransactionDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('transaction:index')