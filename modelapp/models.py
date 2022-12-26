from django.db import models
from modelapp.validators import first_letter,Minchar
# Create your models here.
class Bookmodel(models.Model):
    book_id=models.CharField(max_length=20,primary_key=True, validators=[first_letter])
    book_name=models.CharField(max_length=40,blank=True)
    author_name=models.CharField(max_length=30, validators=[first_letter,Minchar])
    publication=models.CharField(max_length=40, validators=[first_letter,Minchar])
    Release_date=models.DateField()
    list=[['Drama','Drama'],['crime','crime'],['thriller','thriller'],['biography','biography']]
    genera=models.CharField(max_length=50,choices=list,null=False,default='none')
    price=models.PositiveIntegerField()