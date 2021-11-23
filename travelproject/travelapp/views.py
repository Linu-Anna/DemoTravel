

from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import person

def demo(request):
        obj=place.objects.all()
        obj1=person.objects.all()
        return render(request,'index.html',{'result':obj,'value':obj1})
