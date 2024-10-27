from django.db import models

from Category.models import Category
from SubCategory.models import Subcategory


# Create your models here.
class Product(models.Model):

    product_id = models.AutoField(db_column='product_id',primary_key=True,null=False)
    product_name = models.CharField(db_column='product_name',max_length=255,default="",null=False)
    product_description = models.CharField(db_column='product_description',max_length=255,default="",null=False)
    product_price = models.FloatField(db_column='product_price',default=0,null=False)
    product_image_name = models.ImageField(upload_to='static/product/',db_column='product_image_name',max_length=255,default="",null=False)
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE,db_column='product_category_id',null=False)
    product_subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE,db_column='product_subcategory_id',null=False)


    def __str__(self):
        return '{} - {} - {} - {}'.format(self.product_name, self.product_description,self.product_price,self.product_image_name)

    def __as_dict__(self):
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "product_description": self.product_description,
            "product_price": self.product_price,
            "product_image_name": self.product_image_name,
            "product_category": self.product_category,
            "product_subcategory": self.product_subcategory
        }

    class Meta:
        db_table = "product_table"