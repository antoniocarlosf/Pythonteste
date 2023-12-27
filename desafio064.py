total = 0
contagem = 0
numero = int(input('Digite um numero ou (999) para sair: '))
while numero != 999:
    total += numero
    contagem += 1
    numero = int(input('Digite outro numero ou (999) para sair: '))
print('Acabou. Voce digitou {} numeros e a soma foi de {}'.format(contagem, total))
