from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime

import random

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
    chosen = int(request.GET['number']) #select에서 입력한수가 chosen에 담김
    
    results=[]
    if chosen >=1 and chosen <=45:
        results.append(chosen)
    
    box =[]
    for i in range(0,45):
        if chosen !=i+1:
            box.append(i+1)
    
    random.shuffle(box)

    while len(results) < 6:
        results.append(box.pop())

    context ={
        'numbers' : results
    }
    return render(request,'first/result.html',context)