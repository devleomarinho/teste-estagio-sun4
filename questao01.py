#Opção A: Usei a função set() para converter a lista nums em um set, estrutura que não permite itens duplicados, e em seguida usei a
# função list() para converter o set em uma lista novamente

def q1_remover_duplicados(nums):
    nums = list(set(nums))
    return nums

print("Opção A:")
print(q1_remover_duplicados([1, 2, 2, 3, 4, 4, 5]))

#Opção B: Criei uma lista vazia e em seguida fiz um loop na lista original que a função recebe (nums) e, caso o número não esteja presente na lista
# o adiciona na lista vazia. No final, retorna esta lista sem os duplicados

def q1b_remover_duplicados(nums):
    sem_duplicados = []

    for num in nums:
        if num not in sem_duplicados:
            sem_duplicados.append(num)
    return sem_duplicados

print("Opção B:")
print(q1b_remover_duplicados([1, 2, 2, 3, 4, 4, 5]))