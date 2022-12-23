from django.db import models

# Create your models here.
class Bookmodel(models.Model):
    book_id=models.CharField(max_length=20,primary_key=True)
    book_name=models.CharField(max_length=40,blank=True)
    author_name=models.CharField(max_length=30)
    publication=models.CharField(max_length=40)
    Release_date=models.DateField()
    list=[['Drama','Drama'],['crime','crime'],['thriller','thriller'],['biography','biography']]
    genera=models.CharField(max_length=50,choices=list,null=False,default='none')
    price=models.PositiveIntegerField()