from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=255)
    product_url = models.URLField()
    image_url = models.URLField()   
    description = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    in_stock = models.BooleanField('In Stock', default=True)
    price_drop_threshold = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField('Active', default=True)
    retailer = models.ForeignKey('Retailer', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.price
    
class Retailer(models.Model):
    name = models.CharField(max_length=200)
    merchant_url = models.URLField()
    def __str__(self):
        return self.name
    
class Wishlist(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product_id.name
    
