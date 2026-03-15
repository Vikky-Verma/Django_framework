from django.db import models
from django.utils import timezone # Import timezone to handle date and time fields
from django.contrib.auth.models import User # Import User model to associate chai varieties with users if needed

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML' , 'MASALA'),
        ('GR' , 'GINGER'),
        ('KL' , 'KIWI'),
        ('PL' ,'PLAIN'),
        ('EL' , 'ELAICHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now) # Add a date_added field to track when the chai variety was added
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE) # Add a type field to specify the type of chai variety
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
    
#One to many relationship between User and ChaiVariety (if you want to associate chai varieties with users)
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username} review for {self.chai.name}"
    

# Many to Many relationship between Store and ChaiVariety

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores') # Many to Many relationship between Store and ChaiVariety
    
    def __str__(self):
        return self.name
    
    
# one to one 

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate') # One to One relationship between ChaiVariety and ChaiCertificate
    certificate_number = models.CharField(max_length=50)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()
    
    def __str__(self):
        return f"Certificate for {self.chai.name}"