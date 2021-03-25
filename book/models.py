from django.db import models
from django.urls import reverse

# Create book model
class Book(models.Model):
    book_title = models.CharField(max_length=100)
    book_type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.IntegerField()

    # get a spesific detail of book by primary key
    def get_absolute_url(self):
        return reverse("book:detail", kwargs={"pk": self.pk})

    # Show output   
    def __str__(self):
        return self.book_title
    
class Stock(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return self.stock
    