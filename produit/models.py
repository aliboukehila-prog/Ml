from django.db import models

# Create your models here.
# blog/models.py
from django.db import models

class Produit(models.Model):
    designation = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    
