from django.shortcuts import render,redirect
from Category.models import Category
from SubCategory.models import Subcategory


def load_subcategory(request):

    category_vo_list = Category.objects.all()
    return render(request,"SudCategoryinsert.html",{"category_vo_list": category_vo_list})


def insert_subcategory(request):
    subcategory_category_id = request.POST.get("category_id")
    print("<<<<<<<<<<<<<<<<<<<<<<",subcategory_category_id)
    subcategory_name = request.POST.get("subcategory_name")
    subcategory_description = request.POST.get("subcategory_description")
    category_vo = Category.objects.get(category_id=subcategory_category_id)
    subcategory_vo = Subcategory()
    subcategory_vo.subcategory_category = category_vo
    subcategory_vo.subcategory_name = subcategory_name
    subcategory_vo.subcategory_description = subcategory_description
    print(subcategory_vo.subcategory_description)
    subcategory_vo.save()
    return redirect(view_subcategory)
# Create your views here.


def view_subcategory(request):
    subcategory_vo_list = Subcategory.objects.all()
    print("<<<<<<<<<<<<<<",subcategory_vo_list)
    return render(request, "ViewSubcategoryinsert.html", context={"subcategory_vo_list": subcategory_vo_list})

def delete_subcategory(request):
    subcategory_vo = Subcategory()
    subcategory_id = request.GET.get("subcategory_id")
    subcategory_vo.subcategory_id = subcategory_id
    subcategory_vo.delete()
    return redirect(view_subcategory)

def edit_subcategory(request):

    subcategory_id = request.GET.get("subcategory_id")
    subcategory_vo_list = Subcategory.objects.filter(subcategory_id=subcategory_id).all()
    print("<<<<<<<>>>>>>>>>",subcategory_vo_list)
    category_vo_list=Category.objects.all()

    return render(request,"edit_subCategory.html",context={"subcategory_vo_list":subcategory_vo_list,"category_vo_list":category_vo_list})

def update_subcategory(request):
    subcategory_vo = Subcategory()

    subcategory_id = request.POST.get("subcategory_id")
    subcategory_category_id = request.POST.get("category_id")
    print("<<<<<<<<<<<<<<<<<<<<<<<<",subcategory_category_id)
    category_vo = Category.objects.get(category_id=subcategory_category_id)
    print("subcategory_id",subcategory_id)
    subcategory_vo.subcategory_category_vo = category_vo
    subcategory_vo.subcategory_id = subcategory_id
    subcategory_vo.subcategory_name = request.POST.get("subcategory_name")
    subcategory_vo.subcategory_description = request.POST.get("subcategory_description")
    subcategory_vo.save()
    return redirect(view_subcategory)