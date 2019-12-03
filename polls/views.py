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
#'processo': '5000404-31.2018.4.02.5112',
 #   'orgao_julgador': 'Juízo Federal da 4ª VF do Rio de Janeiro',
  #  'classe_da_acao': 'MANDADO DE SEGURANÇA',
    # 'data_autuacao': '27/07/2018 16:09:08',
    # 'situacao': 'MOVIMENTO',
    # 'juiz': 'ANDREA DAQUER BARSOTTI',
    # 'processos_relacionados': '5000404-31.2018.4.02.5112/TRF2	|	Relacionado no 2o. grau'
def extracao(request):
    if request.method =='POST':
        url=request.POST['link']
        html = urlopen(url)
        res = BeautifulSoup(html.read(),"html5lib")
        tags =res.find_all('fieldset',id='fldAssuntos')
        #print(tags.getText())
        dados_lista = []
        for tag in tags:
            dados_lista.append(tag.getText())
        #separar = tags.split()
        #print(separar)
       # lista_dados = ['processo','orgao_julgador']
        #for separar in lista_dados:
        return render(request,'polls/extracao.html',{'dados':dados_lista})
    else:
        return render(request,'polls/link.html')
        
