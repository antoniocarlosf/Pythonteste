matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lin in range(0, 3):
    for colun in range(0, 3):
        matriz[lin][colun] = int(input(f'Digite um valora para [{lin}, {colun}]: '))
print('=-' * 30)
for lin in range(0, 3):
    for colun in range(0, 3):
        print(f'[{matriz[lin][colun]:^5}]', end='')
    print()
    