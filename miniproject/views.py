from django.http import HttpResponse
from django.shortcuts import render
import operator 
# Create your views here.
def home(request):
    return render(request,'home.html')
    #return render(request,'home.html')