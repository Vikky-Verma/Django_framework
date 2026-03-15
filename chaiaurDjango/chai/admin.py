from django.contrib import admin
from .models import ChaiVariety, ChaiReview, Store, ChaiCertificate # Import all the models to register them in the admin site

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2 # Number of extra forms to display for adding new reviews

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'date_added') # Display these fields in the admin list view
    inlines = [ChaiReviewInline] # Include the ChaiReview inline to manage reviews directly from the ChaiVariety admin page


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location') # Display these fields in the admin list view
    filter_horizontal = ('chai_varieties',) # Use a horizontal filter widget for the ManyToMany relationship with ChaiVariety


class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issued_date', 'valid_until') # Display these fields in the admin list view   
    
    
    
admin.site.register(ChaiVariety, ChaiVarietyAdmin) # Register the ChaiVariety model to make it accessible in the admin site
admin.site.register(ChaiReview) # Register the ChaiReview model to make it accessible in the admin site
admin.site.register(Store, StoreAdmin) # Register the Store model to make it accessible in the admin site
admin.site.register(ChaiCertificate, ChaiCertificateAdmin) # Register the ChaiCertificate model to make it accessible in the admin site
