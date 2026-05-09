'''Pedir números ao usuário até 0 ser digitado. Ao final, informar o maior número: '''

maior = None

num = float(input("Digite um número (0 para parar): "))

while num != 0:
    if maior is None or num > maior:
        maior = num
    
    num = float(input("Digite um número (0 para parar): "))

if maior is not None:
    print(f"Maior número: {maior}")
else:
    print("Nenhum número foi digitado.")