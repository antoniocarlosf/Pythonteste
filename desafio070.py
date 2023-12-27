print('-'*30)
print('Loja do Sr.Geremias')
print('-'*30)
total = 0
produtos = 0
caro = 0
menor_preco = float('inf')

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    escolha = input('Quer continuar? [S/N]: ').upper()
    while escolha not in ('S', 'N'):
        escolha = input('Quer continuar? [S/N]: ').upper()

    if preco >= 1000:
        caro += 1

    total += preco

    if preco < menor_preco:
        menor_preco = preco
        produto_menor = produto
    if escolha == 'N':
        print('====== FIM DO PROGRAMA ======')
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {caro} custando mais de R$1000.00 ')
print(f'O prduto mais barato foi {produto_menor} que custa R${menor_preco}')
