distancia = float(input('Qual a distancia da viagem? '))
print('Voce esta prestes a começar uma viagem de {}Km.'.format(distancia))
preço = distancia * 0.50 if distancia <=200 else distancia * 0.45
print('E o preço da passagem sera R${}'.format(preço))
