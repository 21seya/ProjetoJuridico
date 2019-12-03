from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import urlopen
from bs4 import BeautifulSoup
#from django.template import loader

#from .models import Question


def index(request):
    return render(request,'polls/index.html')
    #print(request.statuscode)
def layout(request):
    return render(request,'polls/layout.html')    

def extracao(request):
    if request.method =='POST':
        url=request.POST['link']
        html = urlopen(url)
        res = BeautifulSoup(html.read(),"html5lib")
        tags =res.find_all('div')[0].getText()
        print(tags)
        return HttpResponse(tags)
    else:
        return render(request,'polls/link.html')
