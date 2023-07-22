numero_de_numeros = int(input())
sequence = [int(x) for x in input().split(" ")]

def soma_real(list):
    soma = 0
    for num in list:
        soma += num
    return soma

def soma_ideal(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 2 + 1 
    else: return soma_ideal(num - 1) + num

numero_faltante = soma_ideal(numero_de_numeros) - soma_real(sequence)
print(numero_faltante)