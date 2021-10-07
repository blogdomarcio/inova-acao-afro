import pandas as pd
from django.core.management.base import BaseCommand

from banco.models import Agencia


class Command(BaseCommand):

    # Baseado no modelo anterior das pessoas

    help = 'Load agencia data from CSV file'

    def handle(self, *args, **kwargs):
        if Agencia.objects.exists():
            print("A tabela de agencias já foi populada. Nada a fazer.")
        else:
            df = pd.read_csv('bank_accounts.csv')

            data = df['agencia']

            for i in data:
                a = Agencia()
                a.numero = int(i)
                a.save()

                print(f"Agência nº {a}, criada com sucesso!")

        print('\n Processamento concluído')
