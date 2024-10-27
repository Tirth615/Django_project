from django.urls import path
from Product import views

urlpatterns = [

    path('view_product/',views.load,name='view_product/'),

    path('view_product/insert/',views.insert_product,name='insert_product/'),
]