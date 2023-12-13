base = float(input('Quantos metros de largura tem a parede? '))
alt = float(input('E quantos metros de altura ? '))
area = base * alt
pintura = area / 2
print('Voce precisara de {} litros de tinta'.format(pintura))