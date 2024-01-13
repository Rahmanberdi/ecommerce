from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.name





class Order_item(models.Model):
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE , null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0, null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def get_total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.product.name


