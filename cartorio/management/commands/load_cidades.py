import pandas as pd
from django.core.management.base import BaseCommand

from cartorio.models import Estado, Cidade


class Command(BaseCommand):

    help = 'Load contas data from CSV file'

    def handle(self, *args, **kwargs):

        estados = Estado.objects.all()

        # if Conta.objects.exists():

        #     print("\n A tabela de agencias já foi populada. Nada a fazer.")

        # else:

        df = pd.read_csv('Cartorios_utf8.csv', delimiter=';',
                         header=0, index_col=False)

        dadosDIC = df.to_dict('records')

        for e in estados:

            for d in dadosDIC:

                if str(e) == str(d['UF']):

                    try:

                        Cidade.objects.get(nome=str(d['Município']), uf=e.id)
                        print('JA TEM')

                    except:

                        cidade = Cidade()
                        cidade.uf = Estado.objects.get(id=e.id)
                        cidade.nome = str(d['Município'])
                        cidade.save()

        print('\n Processamento concluído')
