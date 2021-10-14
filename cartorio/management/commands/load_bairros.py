import pandas as pd
from django.core.management.base import BaseCommand

from cartorio.models import Estado, Cidade, Bairro


class Command(BaseCommand):

    help = 'Load contas data from CSV file'

    def handle(self, *args, **kwargs):

        cidades = Cidade.objects.all()

        df = pd.read_csv('Cartorios_utf8.csv', delimiter=';',
                         header=0, index_col=False)

        dadosDIC = df.to_dict('records')

        for e in cidades:

            for d in dadosDIC:

                if str(e) == str(d['Município']):

                    try:

                        Bairro.objects.get(nome=str(d['Bairro']), cidade=e.id)
                        print('JA TEM')

                    except:

                        bairro = Bairro()
                        bairro.cidade = Cidade.objects.get(id=e.id)
                        bairro.nome = d['Bairro']
                        bairro.save()

        print('\n Processamento concluído')
