from django.urls import path

from . import views
app_name='modelapp'

urlpatterns=[ 
 path('book/',views.Bookview,name='book'),
 path('bookup/<pk>/',views.Bookupdate,name='bookup'),
]