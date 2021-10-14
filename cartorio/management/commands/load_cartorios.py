from datetime import datetime, date, timedelta

import pandas as pd
from django.core.management.base import BaseCommand
from pandas._libs import json

from cartorio.models import  Cidade, Bairro, Cartorio


class Command(BaseCommand):
    help = 'Load contas data from CSV file'

    def handle(self, *args, **kwargs):

        bairros = Bairro.objects.all()

        df = pd.read_csv('Cartorios_utf8.csv', delimiter=';',
                         header=0, index_col=False)

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

        print('\n Processamento concluído')
