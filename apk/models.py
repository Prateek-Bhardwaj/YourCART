from django.db import models
from cloudinary.models import CloudinaryField
import datetime
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=198, null=True, blank=True)
    
    def __str__(self):
        return self.title
    

class Product(models.Model):
    name = models.CharField(max_length=198, null=True, blank=True)
    discription = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7 ,decimal_places=2  ,null=True, blank=True)
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + str(self.price)

    @staticmethod
    def get_product_by_Id(ids):
        return Product.objects.filter(id__in = ids)
        

class Picture(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=198, null=True, blank=True)
    picture = models.ImageField(upload_to='static/images/', blank=True, null=True)

    def __str__(self):
        return self.product.name + ' ' + self.title


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.CharField(max_length=198, null=True, blank=True)
    content = models.CharField(max_length=198, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Review on \"'+self.product.name + '\" by '+ self.customer
  

class Booking(models.Model):
    STATUS = {
        ('Pending','Pending'),
        ('Completed', 'Completed'),
    }
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    customer = models.CharField(max_length=198, null=True, blank=True)
    price = models.DecimalField(max_digits=7 ,decimal_places=2  ,null=True, blank=True)
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=198, default='Pending', choices=STATUS)
    
    def __str__(self):
        return self.customer +' - '+ self.product.name 
    
