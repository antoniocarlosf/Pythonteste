ex = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
      'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Escolha um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        print('Tente novamente, ', end='')
    print(f'Voce digitou o numero {ex[n]}')
    opcao = input('Quer continuar? [S/N]: ').upper()
    while opcao not in ('S', 'N'):
        opcao = input('Quer continuar? [S/N]: ').upper()
    if opcao == 'N':
        break
print('Acabou')
