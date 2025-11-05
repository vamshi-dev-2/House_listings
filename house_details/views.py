from django.shortcuts import HttpResponse,render,redirect
from app1.forms import HouseForm
from app1.models import House

def default(request,unmatched):
    return render(request,'default.html')