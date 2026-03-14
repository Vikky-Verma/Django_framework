from django.shortcuts import render 
from .models import ChaiVariety # Import the ChaiVariety model to use it in the views
from django.shortcuts import  get_object_or_404 # Import get_object_or_404 to handle cases where a chai variety is not found

# Create your views here.

def all_chai(request):
    chais = ChaiVariety.objects.all() # Retrieve all chai varieties from the database
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id) # Retrieve a specific chai variety based on the provided ID
    return render(request, 'chai/chai_detail.html', {'chai': chai})