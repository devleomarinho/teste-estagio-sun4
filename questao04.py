def q4_converter_arrays_em_dict(arr1, arr2):
    dict = {}

    for index in range(len(arr1)):
        dict[arr1[index]] = arr2[index]

    return dict


CHAVES = ['data_distribuicao', 'valor_da_causa', 'classe_judicial', 'assunto']
VALORES = ['14/04/2024', 'R$ 810,26', 'EXECUÇÃO DE TÍTULO EXTRAJUDICIAL (12154)', 'Nota Promissória (4980)']
print(q4_converter_arrays_em_dict(CHAVES, VALORES))