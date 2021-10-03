import json
from datetime import date, datetime

import requests
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from anymail.message import attach_inline_image_file

# Create your views here.
from sweetify import sweetify

from inovacao_afro.settings import ALPHA_API
from web.models import Curriculo, Skill, Education, Experience, Portifolio, Mensagem


def index(request):
    return render(request, 'index.html')


def consulta(request):
    if request.POST:

        empresa = request.POST['symbol']

        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=" + empresa + "&outputsize=full&apikey=" + ALPHA_API
        r = requests.get(url)

        if r.status_code == 200:

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
                sweetify.error(request, 'Data não contem registros!',
                               text='Tente Novamente!',
                               persistent='Fechar')

            return render(request, 'consulta.html')

        elif r.status_code == 11001:

            sweetify.error(request, 'Site Indisponível!',
                           text='Tente Novamente mais tarde!',
                           persistent='Fechar')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


        else:

            sweetify.error(request, 'Site Indisponível!',
                           text='Tente Novamente mais tarde!',
                           persistent='Fechar')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:

        context = {

            'data': '',

        }

        return render(request, 'consulta.html', context)

        # return HttpResponse(json.dumps(data), content_type="application/json")


def curiculo(request):
    curriculo = Curriculo.objects.first()
    skils = Skill.objects.filter(person=curriculo)
    educations = Education.objects.filter(person=curriculo)
    experiences = Experience.objects.filter(person=curriculo)
    portfifolio1 = Portifolio.objects.filter(person=curriculo, categoria='Web')[0:2]
    portfifolio2 = Portifolio.objects.filter(person=curriculo, categoria='Web')[2:4]
    portfifolio3 = Portifolio.objects.filter(person=curriculo, categoria='Photo')[0:2]
    portfifolio4 = Portifolio.objects.filter(person=curriculo, categoria='Photo')[2:4]
    portfifolio5 = Portifolio.objects.filter(person=curriculo, categoria='Graphic')[0:2]
    portfifolio6 = Portifolio.objects.filter(person=curriculo, categoria='Graphic')[2:4]

    context = {
        'curriculo': curriculo,
        'skils': skils,
        'educations': educations,
        'experiences': experiences,
        'portfifolio1': portfifolio1,
        'portfifolio2': portfifolio2,
        'portfifolio3': portfifolio3,
        'portfifolio4': portfifolio4,
        'portfifolio5': portfifolio5,
        'portfifolio6': portfifolio6,
    }
    return render(request, 'curriculo/index.html', context)


def email(request):
    if request.POST:

        m = Mensagem()
        m.nome = request.POST['name']
        m.email = request.POST['email']
        m.assunto = request.POST['assunto']
        m.mensagem = request.POST['message']

        m.save()

        contato = request.POST['email']

        msg = EmailMultiAlternatives(
            subject="Mensagem Enviada com Sucesso",
            body="InovAção Afro - CESAR - SHARE RH",
            from_email="Claudio Marcio @blogdomarcio -  <naoresponda@marcioweb.com.br>",
            to=[contato],
            reply_to=["Suporte <blogdomarcio@live.com>"])

        # Include an inline image in the html:
        # logo_cid = attach_inline_image_file(msg, "fotos/educa.png")
        html = """"
        
        <p>Olá {responsavel},</p>
        <p> A sua mensagem foi enviada! </p>
        <hr>
        <p><strong>@blogdomarcio</strong></p>
        <p> blogdomarcio@live.com | (77)77999641685
        <br>
        <p></p>""".format(responsavel=request.POST['name'])
        msg.attach_alternative(html, "text/html")

        # Optional Anymail extensions:
        msg.metadata = {"user_id": "8675309", "experiment_variation": 1}
        msg.tags = ["activation", "onboarding"]
        msg.track_clicks = True

        # Send it:
        msg.send()

        sweetify.success(request, 'Email Enviado com sucesso')

        return redirect('/')
