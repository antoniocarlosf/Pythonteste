n1 = int(input('Escolha um numero para a tabuada: '))

for x in range(1, 11):
  print('{}x{}={}'.format(n1, x, (x*n1)))
