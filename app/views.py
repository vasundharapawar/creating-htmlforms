from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def htmlform(request):
    return render(request,'htmlform.html')


def create_school(request):
    
    if request.method=='POST':
        sn=request.POST['sn']
        sl=request.POST.get('sl')
        sp=request.POST.get('sp')

        SO=School.objects.get_or_create(Sname=sn,Slocation=sl,Sprincipal=sp)[0]
        SO.save()

        return HttpResponse('School data is inserted')

    return render(request,'create_school.html')

