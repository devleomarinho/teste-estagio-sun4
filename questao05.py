from datetime import datetime, timedelta

def q5_calculo_prazo(data, prazo, tipo):

    data_inicial = datetime.strptime(data, '%d/%m/%Y')
    data_inicial_format = data_inicial.strftime('%d/%m/%Y')

    if tipo.upper() == 'CORRIDOS':

        data_final = data_inicial + timedelta(days=prazo)
        data_final_corridos = data_final.strftime('%d/%m/%Y')
        return (f"Data inicial: {data_inicial_format}, prazo de {prazo} dias corridos, a data final é no dia {data_final_corridos}")

    elif tipo.upper() == 'UTEIS':
        data_final_uteis = data_inicial
        dias_uteis = 0

        while dias_uteis < prazo:
            data_final_uteis += timedelta(days=1)
            if data_final_uteis.weekday() < 5:
                dias_uteis += 1


        data_final_uteis = data_final_uteis.strftime('%d/%m/%Y')
        return (f"Data inicial: {data_inicial_format}, prazo de {prazo} dias úteis, a data final é no dia {data_final_uteis}")



print(q5_calculo_prazo("16/09/2024", 7, "UTEIS"))
print(q5_calculo_prazo("16/09/2024", 7, "CORRIDOS"))
