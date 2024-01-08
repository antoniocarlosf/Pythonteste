galera = list()
dado = list()
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    r = str(input('Quer continuar? [S/N] ')).upper()
    galera.append(dado[:])
    dado.clear()
    if r == 'N':
        break

pesol = galera[0][1]
pesop = galera[0][1]

for p in galera:
    if p[1] > pesop:
        pesop = p[1]
        print(f'O maior peso foi de {pesop}. Peso de {p[0]}')
    elif p[1] < pesol:
        pesol = p[1]
        print(f'O menor peso foi de {pesol}. Peso de {p[0]}')
