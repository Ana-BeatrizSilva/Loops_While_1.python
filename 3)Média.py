'''Pedir vários números e parar quando digitar -1. Calcular a média dos números digitados (sem contar o -1):'''

soma = 0
contagem = 0

num = float(input('Informe um número: '))
while num != -1:
    contagem += 1
    soma += num
    num = float(input('Informe um número: '))

if contagem > 0:
    media = soma/contagem
    print(f'A média é: {media}')