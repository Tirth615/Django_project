from django.urls import path
from Category import views

urlpatterns = [
    path("",views.hello),

    path("add_category/", views.add_category,name= 'add_category/'),

    path("view_category/",views.view_category,name= "view_category/"),

    path("insert_category/",views.insert_category),

    path("delete_category",views.delete_category),

    path("edit_category",views.edit_category),

    path("update_category/",views.update_category),

    # path("sub_category/", views.sub_category,name= 'sub_category/')

]

