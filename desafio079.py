valor = []

while True:
    n = int(input('Digite um valor: '))
    if n not in valor:
        valor.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não sera adicionado')
    r = (input('Quer continuar? [S/N] ')).upper()
    if r == 'N':
        print(f'Voce digitou os valores {sorted(valor)}')
        break
