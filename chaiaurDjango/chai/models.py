from django.db import models
from django.utils import timezone # Import timezone to handle date and time fields

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
