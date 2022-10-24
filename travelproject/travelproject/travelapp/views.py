from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Placemeet


# Create your views here.
def demo(request):
   # name='india'
    obj=Place.objects.all()
    obj1=Placemeet.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
#def addition(request):
   # x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #adds=x+y
   # sub=x-y
   # mul=x*y
  #  div=x/y
   # return render(request,"result.html",{'result':adds,'resultsub':sub,'resultmul':mul,'resultdiv':div})