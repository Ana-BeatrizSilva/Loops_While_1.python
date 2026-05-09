'''Mostrar tabuada de 1 a 10 de um número: '''

num = int(input("Digite um número: "))
contador = 1

while contador <= 10:
    print(f"{num} x {contador} = {num * contador}")
    contador += 1