primeiro = int(input('Primeiro termo:  '))
razao = int(input('Razão:  '))
decimo = primeiro + (9 + 1) * razao
c = primeiro
while c <= decimo:
    print('{} '.format(c), end=' ')
    c += razao
while True:
    print('\nQuantos termos mais voce quer ver? Se não quiser ver mais nenhum, digite [0]')
    escolha = int(input('Opção: '))
    mais = c + escolha * razao
    while c < mais:
        print('{}'.format(c), end=' ')
        c += razao
    if escolha == 0:
        print('Encerrado')
        break
