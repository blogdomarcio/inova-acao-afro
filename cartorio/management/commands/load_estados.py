import pandas as pd
from django.core.management.base import BaseCommand

from cartorio.models import Estado


class Command(BaseCommand):

    # Baseado no modelo anterior das pessoas

    help = 'Load estados data from CSV file'

    def handle(self, *args, **kwargs):
        if Estado.objects.exists():
            print("A tabela de agencias já foi populada. Nada a fazer.")
        else:

            # col_names = ["UF", "CNPJ", "CNS", "Data de Instalação",  "Nome Oficial", "Nome Fantasia", "Endereço", "Bairro", "Município", "CEP", "Nome do Titular", "Nome do Substituto",
            #              "Nome do Juiz", "Homepage", "Email", "Telefone", "Fax", "Observação", "Última Atualização", "Horário de Funcionamento", "Área de Abrangência", "Atribuições", "Comarca"]

            df = pd.read_csv('Cartorios_utf8.csv',
                             delimiter=';', header=0, index_col=False)

            # data = df["UF"]

            dadosDIC = df.to_dict('records')

            # print(len(list(iter(df))), len(list(iter(df))))

            # print(data[0])

            for i in dadosDIC:
                try:
                    Estado.objects.get(sigla=i['UF'])
                    print('JA TEM')
                except:
                    a = Estado()
                    a.sigla = i['UF']
                    a.save()
                    print('Salvo')

           ########################

            # for i in data:
            #     a = Agencia()
            #     a.numero = int(i)
            #     a.save()

            #     print(f"Agência nº {a}, criada com sucesso!")

        print('\n Processamento concluído')
