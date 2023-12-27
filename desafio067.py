n1 = int(input('Digite um numero para tabuada: '))
while True:
    for x in range(1, 11):
        print(f'{n1}x{x}={(x*n1)}')
    escolha = int(input('Quer ver a tabuada de qual outro valor? '))
    if escolha <= 0:
        print('A tabuada não aceita numeros nulos ou negativos! Encerrado')
        break

    n1 = escolha
