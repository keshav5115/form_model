from django import forms
from .models import Bookmodel


class BookForm(forms.ModelForm):
    class Meta:
       model=Bookmodel
       fields='__all__'
    #    fields=['book_name','author_name','genera','price',]
    #    exclude=['book_id','publication']
       list=[['Drama','Drama'],['crime','crime'],['thriller','thriller'],['biography','biography']]
       widgets={'Release_date':forms.DateInput(attrs={'type':'date'}),
            
                'book_name':forms.TextInput(attrs={'placeholder':'bookname ','title':'book name please','class':'formfield'}),
                'author_name':forms.TextInput(attrs={'placeholder':'Author name ','title':'Author name please','class':'formfield'}),}


    def clean(self):
        bookname=self.cleaned_data['book_name']
        bookid=self.cleaned_data['book_id']
        if not(6<=len(bookname)<=20):
            raise forms.ValidationError('the number of characters of bookname should be in the range of 6 to 20')
        
        if not(bookid[:4].isalpha()and bookid[4:].isnumeric() and len(bookid)==7)  :
            raise forms.ValidationError('book id should contain both alphabets and numbers')
