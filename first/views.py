from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    context={
        'current_date' : now
    }  # 동적으로 삽입가능하게 하기위한 object
    return render(request,'first/index.html',context)


def select(request):
    context={
        'number' : 4
    } 
    return render(request,'first/select.html',context)


def result(request):
    context={ 'numbers' : [1,2,3,4,5,6]
    } 
    return render(request,'first/result.html',context)