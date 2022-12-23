from django import forms
from .models import Bookmodel


class BookForm(forms.ModelForm):
    class Meta:
       model=Bookmodel
       fields='__all__'
    #    fields=['book_name','author_name','genera','price',]
    #    exclude=['book_id','publication']
       widgets={'Release_date':forms.DateInput(attrs={'type':'date'}),
                'genera':forms.CheckboxSelectMultiple(),
                'book_name':forms.TextInput(attrs={'placeholder':'bookname ','title':'book name please','class':'formfield'}),
                'author_name':forms.TextInput(attrs={'placeholder':'Author name ','title':'Author name please','class':'formfield'}),}


