from django.db import models
from book.models import Book
from costumer.models import Costumer
from django.urls import reverse

# Create transaction model

class Payment(models.Model):
    payment_method = models.CharField(max_length=50)

    # Show output
    def __str__(self):
        return self.payment_method

class Order(models.Model):
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    payment =models.ForeignKey(Payment, on_delete=models.CASCADE)
    total_price = models.IntegerField()

    # get a spesific detail of book by primary key
    def get_absolute_url(self):
        return reverse("transaction:detail", kwargs={"pk": self.pk})