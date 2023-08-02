from django.shortcuts import render
from app.forms import *
# Create your views here.

from django.views.generic import View,TemplateView
from django.http import HttpResponse

class Data_render(View):
    def get(self,request):
        d={'name':'vani'}
        return render(request,'data_render.html',d)
    
def insert_fbv(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Data inserted')
    return render(request,'insert_fbv.html',d)

class insert_cbv(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'insert_cbv.html',d)
    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid:
            SFD.save()
            return HttpResponse('insert_cbv')
        
class temp(TemplateView):
    template_name='temp.html'