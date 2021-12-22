login = 'alex'
senha = '1234'

entra_login = raw_input('Digite seu login: ')
entra_senha = raw_input('Digite sua senha: ')

if entra_login == login and entra_senha == senha:
    print 'Sistema conectado'
else:
    print 'Login incorreto'