from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# index is conventionally the main page
# The function parameter is http request sent by web-browser to our web-server. Django takes this request and sends it to our view function
# /products -> index
# URL (uniform resource relocator)


def index(request):
    products = Product.objects.all()
    # return HttpResponse('Hello World')
    return render(request,
                  'index.html',
                  {'products': products})  # A dictionary that contains data to be passed to the template


def new(request):
    return HttpResponse('New Products')

