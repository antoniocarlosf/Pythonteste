from time import sleep
from random import randint
tentativas = 1
computador = randint(0, 10)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
sleep(2)
jogador = int(input('Em que numero eu pensei? '))
while jogador != computador:
    jogador = int(input('Errou! Tente outra vez: '))
    tentativas += 1
print('Parabens! voce acertou. Voce precisou de {} tentativas'.format(tentativas))
