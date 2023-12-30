num = (int(input('Escolha um numero: ')),
       int(input('Escolha outro: ')),
       int(input('Outro numero: ')),
       int(input('Mais um: ')))
print(f'Voce digitou os valores {num}')
if 9 in num:
    print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu em {num.index(3) + 1}°')
else:
    print('O valor 3 não apareceu')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')