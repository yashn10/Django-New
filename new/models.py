from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, default='')
    # subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=False, default='')
    image = models.ImageField(upload_to='ecommerce/ping')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    contact = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])
    password = models.CharField(max_length=128)  # Increase length to store hashed passwords
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    