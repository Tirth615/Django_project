from django.shortcuts import render,redirect

import Category
import Product
from Category.models import Category
from Product.models import Product
from SubCategory.models import Subcategory


# Create your views here.

def load(request):
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()
    return render(request,"addproduct.html",context={"category":category,"subcategory":subcategory})

def insert_product(request):
    product = Product()
    product_category_id = request.POST.get("productCategoryId")
    product_subcategory_id = request.POST.get("subcategoryid")
    product.product_name = request.POST.get("product_name")
    product.product_description = request.POST.get("product_description")
    product.product_quantity = request.POST.get("product_quantity")
    product.product_price = request.POST.get("product_price")
    product.product_image = request.FILES["product_image"]
    category = Category.objects.get(category_id=product_category_id)
    subcategory = Subcategory.objects.get(subcategory_id=product_subcategory_id)
    product.product_category = category
    product.product_subcategory = subcategory
    product.save()

    # return redirect('/admin/view_product')
    # return redirect('/admin/view_product')

    return render(request,"hello.html")