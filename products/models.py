from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Variant(models.Model):
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
