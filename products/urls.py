from . import views
from django.urls import path

app_name='products'
urlpatterns = [
    path('',views.product,name='product')
]