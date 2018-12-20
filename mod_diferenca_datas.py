
# Modulo de cálculo de diferença entre datas
# por padrão faz a diferença baseada na data atual, se os parâmetros opcionais não forem preenchidos
#
# Dependências:
# pip install python-dateutil

from datetime import datetime
from dateutil.relativedelta import relativedelta

def diferenca_anos(dia, mes, ano, dia2=0, mes2=0, ano2=0):

    if dia2 == 0 or mes2 == 0 or ano2 == 0:
        data_atual = datetime.now()
    else:
        data_atual = datetime.strptime("{}-{}-{}".format(int(ano2), int(mes2), int(dia2)), '%Y-%m-%d')

    data_aniversario = datetime.strptime("{}-{}-{}".format(int(ano), int(mes), int(dia)), '%Y-%m-%d')
    return abs(relativedelta(data_atual, data_aniversario).years)

def diferenca_dias(dia, mes, ano, dia2=0, mes2=0, ano2=0):

    if dia2 == 0 or mes2 == 0 or ano2 == 0:
        data_atual = datetime.now()
    else:
        data_atual = datetime.strptime("{}-{}-{}".format(int(ano2), int(mes2), int(dia2)), '%Y-%m-%d')

    data_aniversario = datetime.strptime("{}-{}-{}".format(int(ano), int(mes), int(dia)), '%Y-%m-%d')
    return abs((data_atual - data_aniversario).days)
