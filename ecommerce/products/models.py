from django.db import models
from base.models import BaseModel

# Create your models here.

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True,blank=True)
    #what is slug? A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs. 
    category_description = models.TextField(blank=True, null=True)
    category_image = models.ImageField(upload_to='category_images/', blank=True, null=True)

class Product(BaseModel):
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_stock = models.IntegerField()
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')