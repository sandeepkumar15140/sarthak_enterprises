# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    @staticmethod
    def get_product_by_id(product_id):
        try:
            product = Product.objects.get(pk=product_id)
            return product
        except Product.DoesNotExist:
            return None

    @staticmethod
    def get_all_products():
        return Product.objects.all()
