sexo = input('Qual o seu sexo? (M/F): ')
while sexo not in ['M', 'm', 'F', 'f']:
    sexo = input('Sexo invalido. Por favor digite novamente (M/F): ')
print('Sexo valido!')
