from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class CategoryA(models.Model):
    Categoryname = (
        ('mobile', 'MOBILE'),
        ('laptop', 'LAPTOP'),
        ('tv', 'TV'),
        ('desktop', 'DESKTOP'),
        ('computer', 'COMPUTER'),
    )
    id = models.AutoField(db_column='ID', primary_key=True)
    catagery_name = models.CharField(max_length=10, choices=Categoryname, default='---')

    def __str__(self):
        return self.catagery_name

class Items(models.Model):
    id = models.AutoField(primary_key=True)
    itemname = models.CharField(max_length=100)
    cat =    models.ForeignKey(CategoryA,blank=True, null=True, on_delete=models.DO_NOTHING)
