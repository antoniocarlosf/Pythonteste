pessoas = []
tot_sexo = []
mulheres = []
while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: ')).strip()

    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()

    while pessoa['sexo'] not in 'MF':
        print('Erro! Responda apenas com M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])

    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa)

    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()
    while escolha not in 'SN':
        print('Erro! Responda apenas com S ou N.')
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()

    if escolha == 'N':
        break


tot = sum(pessoa['idade'] for pessoa in pessoas)
media = tot / len(pessoas)

print('-=' * 30)

print(f'A) Ao todo temos {len(pessoas)} cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.')

print(f'C) As mulheres cadastradas foram: ', end='')
for mulher in mulheres:
    print(mulher, end=', ')
print()

print('D) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< Encerrado >>')
