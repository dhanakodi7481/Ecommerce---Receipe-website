from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STATE_CHOICES = (

('Tamilnadu','Tamilnadu'),
('Telangana','Telangana'),
('Kerala','Kerala'),
('Bangalore','Bangalore'),
('Puducherry','Puducherry'),
('Andhra pradesh','Andhra pradesh'),
)


CATEGORY_CHOICES = (
    ('BF', 'Breakfast'),
    ('LN', 'Lunch'),
    ('DI', 'Dinner'),
    ('DE', 'Desserts'),
)

class Products(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    preparation_time = models.TextField()
    description = models.TextField()
    ingredients = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)  
    product_image = models.ImageField(upload_to='product', null=True, blank=True)

    def __str__(self):
        return self.title

class Customer (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	product = models.ForeignKey(Products,on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	
	@property
	def total_cost(self):
		return self.quantity * self.product.discounted_price
     


STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
]

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product}"

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product}"