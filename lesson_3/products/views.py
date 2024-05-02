from django.shortcuts import render
from .models import Category, Products
# Create your views here.


def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def get_products(request, pk):
    try:
        products = Products.objects.all(Category=pk)
        context = {'products': products}
        return render(request, 'products.html', context=context)
    except Exception as e:
     
        print(e)
        return render(request, 'error.html')
    

def detail(request, pk):
    product = Products.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context=context)
