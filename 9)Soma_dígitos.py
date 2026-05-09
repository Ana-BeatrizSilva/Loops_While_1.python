'''Peça um número inteiro positivo ao usuário e calcule a soma dos seus dígitos usando while.
Exemplo: 123 → 1 + 2 + 3 = 6'''

num = int(input("Digite um número inteiro positivo: "))
soma = 0

while num > 0:
    soma += num % 10
    num //= 10

print(f"Soma dos dígitos: {soma}")