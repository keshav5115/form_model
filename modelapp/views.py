from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookForm
from.models import Bookmodel
# Create your views here.

def Bookview(request):
    form=BookForm()
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data is stored')
    return render(request,'Booktemp.html',{'form':form})

def Bookupdate(request,pk):
    obj=Bookmodel.objects.get(book_id=pk)
    form=BookForm(instance=obj)
    if request.method =='POST':
        form=BookForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('data is updated')

    return render(request,'bookupdate.html',{'form':form})
    