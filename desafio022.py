nome = str(input('Digite um nome completo: ')).strip()
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome) -nome.count(' ')))
dividido = nome.split()
print('{} possui {} letras'.format(dividido[0], len(dividido[0])))
