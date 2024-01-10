num = [[], []]
valor = 0
for cont in range(0, 8):
    valor = (int(input(f'Digite o {cont}º valor: ')))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num.sort()
print(f'Os valores pares são {num[1]}')
print(f'Os valores impares são {num[0]}')
