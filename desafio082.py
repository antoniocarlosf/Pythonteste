lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = input('Quer continuar? [S/N]: ').upper()
    if r == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Os numeros digitados foram {lista}')
print(f'Os numeros pares são {pares}')
print(f'Os numeros impares são {impares}')
