from django.contrib import admin
from .models import ChaiVariety # Import the ChaiVariety model to register it in the admin site

# Register your models here.
admin.site.register(ChaiVariety) # Register the ChaiVariety model to make it accessible in the admin site
