
# modulo de cálculo de diferença entre datas
# dependência:
# pip install python-dateutil

from datetime import datetime
from dateutil.relativedelta import relativedelta

def diferenca_anos(dia, mes, ano):

    data_atual = datetime.now()
    data_aniversario = datetime.strptime("{}-{}-{}".format(int(ano), int(mes), int(dia)), '%Y-%m-%d')
    return abs(relativedelta(data_atual, data_aniversario).years)

def diferenca_dias(dia, mes, ano):

    data_atual = datetime.now()
    data_aniversario = datetime.strptime("{}-{}-{}".format(int(ano), int(mes), int(dia)), '%Y-%m-%d')
    return abs((data_atual - data_aniversario).days)
