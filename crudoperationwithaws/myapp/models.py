from django.db import models

# Create your models here.


class ProductDetailsModel(models.Model):
    product_name = models.CharField(max_length=30)
    product_price = models.FloatField()
    product_details = models.CharField(max_length=30)
    product_photo = models.ImageField(upload_to='product_image')
