import pandas as pd
from django.core.management.base import BaseCommand

from cartorio.models import Estado


class Command(BaseCommand):

    help = 'Load estados data from CSV file'

    def handle(self, *args, **kwargs):
        if Estado.objects.exists():
            print("A tabela de agencias já foi populada. Nada a fazer.")
        else:

            df = pd.read_csv('Cartorios_utf8.csv',
                             delimiter=';', header=0, index_col=False)

            dadosDIC = df.to_dict('records')

            for i in dadosDIC:
                try:
                    Estado.objects.get(sigla=i['UF'])
                    print('JA TEM')
                except:
                    a = Estado()
                    a.sigla = i['UF']
                    a.save()
                    print('Salvo')

        print('\n Processamento concluído')
