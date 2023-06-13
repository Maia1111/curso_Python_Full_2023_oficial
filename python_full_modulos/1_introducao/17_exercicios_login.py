# Defina um usuário e senha e depois verifique se o login e senha do usuário é valido

USUARIO = 'admin'
SENHA  = 123


while True:
    usuario_login = input('Usuário: ')
    senha_login = int(input('Senha: '))

    if usuario_login  == USUARIO and senha_login == SENHA:
        print('Bem vindo ao sistema!')
        break
    else:
        print('Usuário ou senha incorreto!')
        continue

