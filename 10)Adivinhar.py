'''Adivinhar número secreto (entre 1 e 10) gerado aleatoriamente: '''

import random

secreto = random.randint(1,10)
secreto_user = int(input('Informe o número secreto: '))

while secreto != secreto_user:
    print('ERRADO')
    secreto_user = int(input('Informe o número secreto: '))
if secreto == secreto_user:
    print('CORRETO')