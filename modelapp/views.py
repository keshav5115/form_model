from django.shortcuts import render
from .forms import BookForm
# Create your views here.

def Bookview(request):
    form=BookForm()
    return render(request,'Booktemp.html',{'form':form})