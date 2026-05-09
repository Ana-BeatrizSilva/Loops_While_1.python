'''Peça ao usuário uma nota entre 0 e 10. Enquanto ele digitar um valor inválido, continue pedindo.
Quando for válido, exiba “Nota aceita": '''

nota = float(input("Digite uma nota (0 a 10): "))

while nota < 0 or nota > 10:
    print("Valor inválido!")
    nota = float(input("Digite uma nota (0 a 10): "))

print("Nota aceita")