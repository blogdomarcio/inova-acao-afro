from datetime import datetime, date, timedelta

import pandas as pd
from django.core.management.base import BaseCommand
from pandas._libs import json

from cartorio.models import Estado, Cidade, Bairro, Cartorio


class Command(BaseCommand):
    help = 'Load contas data from CSV file'

    def handle(self, *args, **kwargs):

        # cidades = Cidade.objects.all()

        bairros = Bairro.objects.all()

        # if Conta.objects.exists():

        #     print("\n A tabela de agencias já foi populada. Nada a fazer.")

        # else:

        df = pd.read_csv('Cartorios_utf8.csv', delimiter=';',
                         header=0, index_col=False)

        # print(df)

        # dadosDIC = df.to_dict('records')

        dadosDIC = json.loads(df.to_json(orient='records'))

        for e in bairros:

            for d in dadosDIC:

                if str(e.nome) == str(d['Bairro']) and str(e.cidade) == str(d['Município']):

                    b = str(d['CEP']).replace('.0', "")

                    c = Cartorio()
                    c.titular =  d['Nome do Titular']
                    c.cnpj = d['CNPJ']
                    c.cns =  d['CNS']
                    c.nome_fantasia = d['Nome Fantasia']
                    c.nome_oficial =  d['Nome Oficial']
                    try:
                        c.data_inst =  datetime.strptime(d['Data de Instalação'], '%d/%m/%Y').date()
                    except:
                        pass

                    try:
                        c.data_ult_atual = datetime.strptime(d['Última Atualização'], '%d/%m/%Y').date()
                    except:
                        pass

                    c.endereco = str(d['Endereço'])
                    c.cep = b
                    c.cidade = Cidade.objects.get(id=e.cidade.id)
                    c.bairro = Bairro.objects.get(id=e.id)

                    c.juiz = d['Nome do Juiz']
                    c.substituto =  d['Nome do Substituto']
                    c.homepage =  d['Homepage']
                    c.email =d['Email']
                    c.telefone =   d['Telefone']
                    c.fax =  d['Fax']
                    c.observacao =  d['Observação']
                    c.horario =  d['Horário de Funcionamento']
                    c.abrangencia = d['Área de Abrangência']
                    c.atribuicoes = d['Atribuições']
                    c.comarca =  d['Comarca']
                    c.entrancia =  d['Entrância']

                    c.save()

                    # print(c.nome_oficial)
                # c.

                # if str(e) == str(d['Bairro']):
                #
                #     try:
                #
                #         Bairro.objects.get(nome=str(d['Endereço']), cep=str(d['Município']), cidade=e.id)
                #         print('JA TEM')
                #
                #     except:
                #
                #         bairro = Bairro()
                #         bairro.cidade = Cidade.objects.get(id=e.id)
                #         bairro.nome = str(d['Endereço'])
                #         bairro.cep = str(d['Município'])
                #         bairro.save()

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
