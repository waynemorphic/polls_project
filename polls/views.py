from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# First view
def index(request):
    return HttpResponse("First view")
