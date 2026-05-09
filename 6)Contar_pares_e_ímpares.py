'''Pedir números até o usuário digitar 0. Contar quantos números são pares e quantos são ímpares: '''

contPar = 0
contImpar = 0
num = int(input('Digite um número: '))

while num != 0:
    if num % 2 == 0:
        contPar += 1
    elif num % 2 != 0:
        contImpar += 1
    num = int(input('Digite um número: '))

print(f'Contagem de números pares: {contPar}')
print(f'Contagem de números ímpares: {contImpar}')