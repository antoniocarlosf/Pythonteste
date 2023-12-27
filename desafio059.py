from time import sleep
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
while True:
    print('''Oque voce quer fazer com os numeros?
    [ 1 ] Somar.
    [ 2 ] Multiplicar.
    [ 3 ] Mostrar maior.
    [ 4 ] Escolher novos numeros.
    [ 5 ] Sair do programa''')

    escolha = int(input('Opção: '))
    sleep(1)
    if escolha == 1:
        soma = n1 + n2
        print('A soma deu: {}'.format(soma))

    elif escolha == 2:
        multiplicado = n1 * n2
        print('A multiplicação deu {}'.format(multiplicado))

    elif escolha == 3:
        if n2 > n1:
            print('O maior numero é {}'.format(n2))
        else:
            print('O maior numero é {}'.format(n1))

    elif escolha == 4:
        n1 = float(input('Troque o primeiro numero'))
        n2 = float(input('Troque o segundo numero'))

    elif escolha == 5:
        print('Programa encerrado!')
        break
    else:
        print('Opção invalida. pro favor escolha uma opção valida.')
