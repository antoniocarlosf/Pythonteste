total = 0
contagem = 0
while True:
    numero = int(input('Digite um numero (ou 999 para encerrar): '))

    if numero == 999:
        print('Encerrado')
        break
    total += numero
    contagem += 1
print(f'Voce digitou {contagem} numeros e a soma foi de {total}')
