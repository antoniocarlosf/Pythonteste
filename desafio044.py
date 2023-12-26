valor = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    desconto = valor * 0.90
    print('O total fica {} com 10% de desconto'.format(desconto))
elif opção == 2:
    desconto2 = valor * 0.95
    print('O valor fica {} com desconto'.format(desconto2))
elif opção == 3:
    print('O valor fica {}'.format(valor))
elif opção == 4:
    valor += valor * 0.20
    print('O valor fica {} com juros'.format(valor))
