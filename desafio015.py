dias = int(input('Quantos dias o carro foi usado? '))
km = float(input('Quantos Km você andou com o carro? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de {:.2f}'.format(pago))