import pandas as pd
from django.core.management.base import BaseCommand

from cartorio.models import Estado, Cidade, Bairro


class Command(BaseCommand):

    help = 'Load contas data from CSV file'

    def handle(self, *args, **kwargs):

        cidades = Cidade.objects.all()

        # if Conta.objects.exists():

        #     print("\n A tabela de agencias já foi populada. Nada a fazer.")

        # else:

        df = pd.read_csv('Cartorios_utf8.csv', delimiter=';',
                         header=0, index_col=False)

        # print(df)

        # data = df["UF"]

        dadosDIC = df.to_dict('records')

        for e in cidades:

            for d in dadosDIC:

                # print(d['Bairro'], d['Município'],  d['Endereço'])

                if str(e) == str(d['Município']):



                    try:

                        Bairro.objects.get(nome=str(d['Bairro']), cidade=e.id)
                        print('JA TEM')

                    except:


                        bairro = Bairro()
                        bairro.cidade = Cidade.objects.get(id=e.id)
                        bairro.nome = d['Bairro']
                        # bairro.cep = b
                        bairro.save()

                        # print(bairro)

                    # print(d['UF'], d['Bairro'],  d['Município'])

        #    for a in agencias:

        #         for d in dadosDIC:

        #             if str(a) == str(d['agencia']):

        #                 conta = Conta()
        #                 conta.agencia = Agencia.objects.get(id=a.id)
        #                 conta.numero = str(d['conta'])
        #                 conta.save()

        #                 print(
        #                     f"Conta nº {conta} criada com sucesso na Agencia nº {conta.agencia}!"
        #                 )

        print('\n Processamento concluído')
