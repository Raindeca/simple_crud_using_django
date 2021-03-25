from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Costumer

# Create generic template
class IndexView(generic.ListView):
    template_name = 'costumer/index.html'
    context_object_name = 'all_costumers'

    # fetch all data in costumer
    def get_queryset(self):
        return Costumer.objects.all()

# read detail data in costumer
class DetailView(generic.DetailView):
    model = Costumer
    template_name = 'costumer/detail.html'
    
# add a new costumer
class CostumerCreate(CreateView):
    model = Costumer
    fields = [
        'name',
        'address',
        'phone_number',
        'email',
    ]

# Update a costumer data 
class CostumerUpdate(UpdateView):
    model = Costumer
    fields = [
        'name',
        'address',
        'phone_number',
        'email',
    ]

# delete a costumer data
class CostumerDelete(DeleteView):
    model = Costumer
    success_url = reverse_lazy('costumer:index')