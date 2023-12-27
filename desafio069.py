print('--'*15)
print('CADASTRE UMA PESSOA')
print('--'*15)
tot = 0
tothomem = 0
totmulher = 0
while True:
    print('-'*15)
    idade = int(input('Idade: '))
    while idade < 0:
        idade = int(input('Idade: '))

    sexo = input('Sexo: [M/F] ').upper()

    while sexo not in ('M', 'F'):
        sexo = input('Sexo: [M/F] ').upper()

    print('-'*15)
    escolha = input('Quer continuar? [S/N] ').upper()

    while escolha not in ('S', 's', 'N', 'n'):
        escolha = input('Quer continuar? [S/N] ').upper()

    if idade >= 18:
        tot += 1
    if sexo == 'M':
        tothomem += 1
    if sexo == 'F' and idade < 20:
        totmulher += 1
    if escolha == 'N':
        print('====== FIM DO PROGRAMA ======')
        break
print(f'Total de pessoas com mais de 18 anos: {tot}')
print(f'Ao todo temos {tothomem} homens cadastrados')
print(f'E temos {totmulher} mulheres com menos de 20 anos')
