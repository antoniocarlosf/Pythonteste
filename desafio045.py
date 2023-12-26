from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA!')
sleep(1)
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0: #Pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Venceu')
    elif jogador == 2:
        print('Computador venceu')
    else:
        print('JOGADA INVALIDA')

elif computador == 1: #Papel
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador venceu')
    else:
        print('JOGADA INVALIDA')

elif computador == 2: #Tesoura
    if jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
        print('Computador venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('JOGADA INVALIDA')
