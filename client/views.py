from django.shortcuts import render
from .models import *

# Create your views here.
HTTP ='http://'



class client:
    def index(request):
        slides = Slide.objects.filter(status=1)
        
            

        news  = New.objects.filter(status=1).order_by('-id')[:4:1]
        
        return render(request,'index.html',{'slides':slides,'news':news})


    def new_detail(request,id,path):
        new     =   New.objects.get(id=id,status=0)
        base_url=   HTTP+request.META['HTTP_HOST']
        date    =   new.updated_at.strftime('%d')
        month    =   new.updated_at.strftime('%b')

        return render(request,'news/detail.html',{'new':new,'base_url':base_url,'date':date,'month':month})
