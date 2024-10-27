from django.urls import path
from SubCategory import views


urlpatterns = [


    path("sub_category/", views.load_subcategory,name= 'sub_category/'),
    path("sub_category/insert_subcategory/",views.insert_subcategory),
    path("sub_category/view_subcategory/",views.view_subcategory,name="sub_category/view_subcategory/"),
    path("delete_subcategory/",views.delete_subcategory,name="delete_subcategory"),
    path("edit_subcategory/update_subcategory/",views.update_subcategory,name="update_subcategory"),
    path("edit_subcategory/",views.edit_subcategory,name="edit_subcategory"),
]