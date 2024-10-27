from django.shortcuts import render,redirect
from Category.models import Category

# Create your views here.

def hello(request):
    return render(request,"hello.html")

def add_category(request):
    return render(request,"addCategory.html")

def insert_category(request):
    category_vo = Category()
    category_vo.category_name = request.POST.get("category_name")
    category_vo.category_description = request.POST.get("category_description")
    category_vo.save()
    return redirect(view_category)

def view_category(request):
    category_vo_list = Category.objects.all()
    return render(request,"viewCategory.html", {"category_vo_list": category_vo_list})

def delete_category(request):
    category_vo = Category()
    category_vo.category_id = request.GET.get("category_id")
    category_vo.delete()
    return redirect(view_category)

def edit_category(request):
    category_id = request.GET.get("category_id")
    category_vo_list = Category.objects.filter(category_id =
                                             category_id).all()
    return render(request,"editCategory.html",{"category_vo_list": category_vo_list})

def update_category(request):
    category_vo = Category()
    category_vo.category_id = request.POST.get("category_id")
    category_vo.category_name = request.POST.get("category_name")
    category_vo.category_description = request.POST.get("category_description")
    category_vo.save()
    return redirect(view_category)
