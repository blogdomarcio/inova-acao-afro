import pandas as pd
from django.core.management.base import BaseCommand

from banco.models import Agencia, Conta


class Command(BaseCommand):

    help = 'Load contas data from CSV file'

    def handle(self, *args, **kwargs):

        agencias = Agencia.objects.all()

        if Conta.objects.exists():

            print("\n A tabela de agencias já foi populada. Nada a fazer.")

        else:

            dados = pd.read_csv('bank_accounts.csv', header=0,
                                squeeze=True)

            dadosDIC = dados.to_dict('records')

            for a in agencias:

                for d in dadosDIC:

                    if str(a) == str(d['agencia']):

                        conta = Conta()
                        conta.agencia = Agencia.objects.get(id=a.id)
                        conta.numero = str(d['conta'])
                        conta.save()

                        print(
                            f"Conta nº {conta} criada com sucesso na Agencia nº {conta.agencia}!"
                        )

            print('\n Processamento concluído')
