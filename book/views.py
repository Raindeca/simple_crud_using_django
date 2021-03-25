from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

# Create generic template
class IndexView(generic.ListView):
    template_name = 'book/index.html'
    context_object_name = 'all_books'

    # fetch all data in book
    def get_queryset(self):
        return Book.objects.all()

# read detail data in book
class DetailView(generic.DetailView):
    model = Book
    template_name = 'book/detail.html'
    
# add a new book
class BookCreate(CreateView):
    model = Book
    fields = [
        'book_title',
        'book_type',
        'category',
        'price',
    ]

# Update a book 
class BookUpdate(UpdateView):
    model = Book
    fields = [
        'book_title',
        'book_type',
        'category',
        'price',
    ]

# delete a book
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book:index')