'''Somar os números digitados pelo usuário e parar quando digitar 0:'''

soma =  0
num = float(input('Informe um número: '))
while num != 0:
    soma += num
    num = float(input('Informe um número: ')) 
print(soma)