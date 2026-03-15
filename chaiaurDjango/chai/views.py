from django.shortcuts import render 
from .models import ChaiVariety, Store # Import the ChaiVariety and Store models to use them in the views
from django.shortcuts import  get_object_or_404 # Import get_object_or_404 to handle cases where a chai variety is not found
from .forms import ChaiVarietyForm # Import the ChaiVarietyForm to use it in the views


# Create your views here.

def all_chai(request):
    chais = ChaiVariety.objects.all() # Retrieve all chai varieties from the database
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id) # Retrieve a specific chai variety based on the provided ID
    return render(request, 'chai/chai_detail.html', {'chai': chai})

def chai_stores_view(request):
    stores = None # Placeholder for store data, you can replace this with actual store data retrieval logic
    if request.method == 'POST':
       form = ChaiVarietyForm(request.POST) # Create a form instance with the submitted data
       if form.is_valid():
           chai_variety = form.cleaned_data['chai_variety'] # Get the selected chai variety from the form
           stores = Store.objects.filter(chai_varieties=chai_variety) # Query the Store model to find stores that carry the selected chai variety
           
           # You can add logic here to find stores that carry the selected chai variety
           # For example, you could query a Store model that has a relationship with ChaiVariety
    else:
       form = ChaiVarietyForm() # Create an empty form instance for GET requests    
    return render(request, 'chai/chai_store.html', {'stores': stores, 'form': form}) # Render the chai store template