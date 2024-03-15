from django.shortcuts import render

# Create your views here.

def checkout(requsest):
    return render(requsest,'cart/checkout.html')