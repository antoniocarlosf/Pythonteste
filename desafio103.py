def ficha():
    nome = input('Nome do Jogador: ')
    gols = input('Numero de Gols: ')

    if nome == '':
        nome += str('<Desconhecido>')
    if gols == '':
        gols += str('0')

    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 30)
ficha()
