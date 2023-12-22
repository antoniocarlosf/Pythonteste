n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
n3 = float(input('Terceira nota'))
n4 = float(input('Quarta nota'))
soma = n1 + n2 + n3 + n4
media = soma / 5
print('Sua média foi de {}'.format(media))
if media < 5.0:
    print('Reprovado!')
if 5.0 <= media <= 6.9:
    print('Recuperação')
if media >= 7.0:
    print('Aprovado')
