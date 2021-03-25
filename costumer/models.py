from django.db import models
from django.urls import reverse

# Create costumer model
class Costumer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    # get a spesific detail of book by primary key
    def get_absolute_url(self):
        return reverse("costumer:detail", kwargs={"pk": self.pk})
    
    # Show output
    def __str__(self):
        return self.name
    