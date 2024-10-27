from django.db import models

# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(db_column="category_id",primary_key=True,null=False)
    category_name = models.CharField(db_column="category_name", max_length=50, default="", null=False)
    category_description = models.TextField(db_column="category_description", max_length=255,default="", null=False)

    def __str__(self):
        return '{} - {}'.format(self.category_name, self.category_description)

    def __as_dict(self):
        return {'category_id': self.category_id,
                'category_name': self.category_name,
                'category_description': self.category_description
                }

    class Meta:
        db_table = 'category_table'