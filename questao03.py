from datetime import datetime
import locale

def q3_tratar_datas(data):

    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    data_tratada = None

    if '/' in data:
        data_tratada = datetime.strptime(data, '%d/%m/%Y')

    elif ' de ' in data:
        data_tratada = datetime.strptime(data, '%d de %B de %Y')

    elif ' ' in data:
        data_tratada = datetime.strptime(data, '%d %b %Y')


    if data_tratada:
        return data_tratada.strftime('%Y-%m-%d')
    else:
        return "Formato de data inválido"


DATAS_PARA_TRATAR = [
    '30/11/2022',
    '01 dez 2022',
    '25/12/2022',
    '31 de dezembro de 2022'
]
for data in DATAS_PARA_TRATAR:
    print(q3_tratar_datas(data))
