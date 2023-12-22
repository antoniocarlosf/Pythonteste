a = int(input('Escolha o primeiro numero: '))
b = int(input('Escolha o segundo numero: '))
menor = b
maior = a
if a < b and b > a:
    print('O menor numero é {} \nE o maior numero é {}'.format(menor, maior))
else:
    print('Não existe valor maior, ambos são iguais')

