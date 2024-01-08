valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print(f'Voce digitou os valors {valores}')
maiorv = max(valores)
menorv = min(valores)
print(f'O maior valor foi {maiorv} nas posições ', end='')
for i, valor in enumerate(valores):
    if valor == maiorv:
        print(f'{i} ... ', end='')
print(f'\n O menor valor foi {menorv}', end='')
for i, valor in enumerate(valores):
    if valor == menorv:
        print(f'{i} ... ', end='')
