from random import randint
from time import sleep

itens = ('Par', 'Impar')
computador = randint(1, 10)
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)
venceu = 0
while True:
    jogador = int(input('Digite um valor: '))
    escolha = input('Par ou Impar? [P/I]: ').strip().upper()
    tot = computador + jogador
    if tot % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Impar'
    print('-'*30)
    print('Computador jogou {} e voce jogou {}. Total de {} deu {}'.format(computador, jogador, tot, resultado))
    print('-'*30)
    print('O resultado é {}'.format(resultado))
    if (escolha == 'P' and resultado == 'Par') or (escolha == 'I' and resultado == 'Impar'):
        venceu += 1
        print('Voce venceu!')
        print('Vamos jogar denovo...')
        print('-='*15)
        sleep(1)
    else:
        print('Voce perdeu!')
        print('-='*15)
        print('GAME OVER! Voce venceu {} vez(es)'.format(venceu))
        break
