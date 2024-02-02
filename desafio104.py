def leiaint(msg):
    while True:
        try:
            numero = int(input(msg))
            return numero
        except ValueError:
            print('\033[1;31m\n Erro! Digite um número inteiro valido \n\033[0m')


# Programa Principal
n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
