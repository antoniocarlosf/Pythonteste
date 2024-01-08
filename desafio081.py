lista = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    escolha = input('Quer continuar? [S/N]').upper()
    if escolha == 'N':
        break

print(f'Voce digitou {len(lista)} elementos ')
if 5 in lista:
    print('O numero 5 esta na lista')
else:
    print('O numero 5 não esta na lista')
lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente é {lista}')
