from django.shortcuts import render
from myapp.models import ProductDetailsModel
import os


# Create your views here.


def show_index(request):
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        product_details = request.POST.get('product_details')
        product_photo = request.FILES['photo']
        ProductDetailsModel(product_name=product_name, product_price=product_price, product_details=product_details,
                            product_photo=product_photo).save()
        return render(request, 'home.html', {"data": ProductDetailsModel.objects.all()})
    else:
        return render(request, 'home.html')


def delete_product(request, product_details):
    data = ProductDetailsModel.objects.get(product_details=product_details)
    data.delete()
    return render(request, "home.html", {"data": ProductDetailsModel.objects.all()})
