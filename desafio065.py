n1 = int(input('Digite um valor '))
n2 = int(input('Outro valor '))
n3 = int(input('Outro valor '))
n4 = int(input('Outro valor '))
n5 = int(input('Outro valor '))
soma = n1 + n2 + n3 + n4 + n5
media = soma / 5
print('A media é {:.2f}'.format(media))
maior = n1
menor = n5
if n1 < n5 and n5 > n1 or n2 < n5 and n5 > n2 or n3 < n5 and n5 > n3 or n4 < n5 and n5 > n4:
    print('O menor numero é {}'.format(maior))
if n2 > n1 and n1 < n2 or n3 > n1 and n1 < n3 or n4 > n1 and n1 < n4 or n5 > n1 and n1 < n5:
    print('O maior numero é {}'.format(menor))
escolha = input('Deseja continuar a escolher valores? [S/N]: ')
while escolha.upper() == 'S':
    valor_novo = int(input('Digite outro valor '))
    soma += valor_novo
    media = soma / 6
    if valor_novo > maior:
        maior = valor_novo
    elif valor_novo < menor:
        menor = valor_novo
    print('A media é {:.2f}'.format(media))
    print('O menor numero é {}'.format(maior))
    print('O maior numero é {}'.format(menor))
    escolha = input('Deseja continuar a escolher valores? [S/N]: ')

print('Programa encerrado.')
