'''Pedir ao usuário para digitar a senha té acertar: '''

senha = '058'
senha_user = input('Digite a senha: ')

while senha != senha_user:
    print('Senha INCORRETA')
    senha_user = input('Digite a senha: ')
if senha == senha_user:
    print('Senha CORRETA')