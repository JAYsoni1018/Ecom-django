from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    category=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    product_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name
    
    
class Contact(models.Model):
    id=models.AutoField(primary_key='true')
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    urself=models.CharField(max_length=300)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    chkbox=models.CharField(max_length=10)
    
    def __str__(self):
        return self.name