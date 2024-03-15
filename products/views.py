from django.shortcuts import render

# Create your views here.
def product(requset):
    return render(requset,'products/product.html')