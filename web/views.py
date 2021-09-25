import json
from datetime import date, datetime

import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from sweetify import sweetify

from inovacao_afro.settings import ALPHA_API


def index(request):
    return render(request, 'index.html')


class HttpReponse(object):
    pass


def consulta(request):
    if request.POST:

        empresa = request.POST['symbol']

        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=" + empresa + "&outputsize=full&apikey=" + ALPHA_API
        r = requests.get(url)

        data = r.json()


        dia = datetime.strptime(request.POST['data'], '%Y-%m-%d').date()

        try:

           pesquisa = data['Time Series (Daily)'][request.POST['data']]

           context = {

               'data': data,
               'dia': dia,
               'empresa': empresa,
               'filto': pesquisa,
               'open': data['Time Series (Daily)'][request.POST['data']]['1. open'],
               'high': data['Time Series (Daily)'][request.POST['data']]['2. high'],
               'low': data['Time Series (Daily)'][request.POST['data']]['3. low'],
               'close': data['Time Series (Daily)'][request.POST['data']]['4. close'],
               'adjusted': data['Time Series (Daily)'][request.POST['data']]['5. adjusted close'],

           }

           return render(request, 'consulta.html', context)

        except:

            pesquisa = ''
            sweetify.error(request, 'Data nao contem registros!',
                           text='Tente Novamente!',
                           persistent='Fechar')



        # print(request.POST['data'])

        context = {

            # 'filto': pesquisa,
            # 'open': data['Time Series (Daily)'][request.POST['data']]['1. open'],
            # 'high': data['Time Series (Daily)'][request.POST['data']]['2. high'],
            # 'low': data['Time Series (Daily)'][request.POST['data']]['3. low'],
            # 'close': data['Time Series (Daily)'][request.POST['data']]['4. close'],
            # 'adjusted': data['Time Series (Daily)'][request.POST['data']]['5. adjusted close'],

        }

        return render(request, 'consulta.html')

    else:

        context = {

            'data': '',

        }

        return render(request, 'consulta.html', context)

        # return HttpResponse(json.dumps(data), content_type="application/json")
