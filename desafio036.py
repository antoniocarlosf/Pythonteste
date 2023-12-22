casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salario? R$ '))
anos = int(input('Em quantos anos planeja pagar? '))
pagar = casa / (anos * 12)
minimo = salario * 30 / 100
print('A prestação mensal sera de R${:.2f}'.format(pagar))
if pagar > minimo:
    print('Prestação mensal excedida pois o minimo é de {}. Emprestimo negado'.format(minimo))
else:
    print('Emprestimo aprovado!')
