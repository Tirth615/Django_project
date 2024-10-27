from django.db import models
from Category.models import Category

# Create your models here.
class Subcategory(models.Model):
    subcategory_id = models.AutoField(db_column='subcategory_id', primary_key=True, null=False)
    subcategory_name = models.CharField(db_column='subcategory_name', max_length=255, default="", null=False)
    subcategory_description = models.CharField(db_column='subcategory_description', max_length=255, default="",null=False)
    subcategory_category = models.ForeignKey(Category,on_delete=models.CASCADE,
                                                db_column='subcategory_category_id',null=False)


    def _str_(self):
        return '{} - {}'.format(self.subcategory_name, self.subcategory_description)

    def as_dict(self):
        return {"subcategory_id": self.subcategory_id,
                "subcategory_name": self.subcategory_name,
                "subcategory_description": self.subcategory_description,
                "subcategory_category": self.subcategory_category
               }


    class Meta:
      db_table = "subcategory_table"