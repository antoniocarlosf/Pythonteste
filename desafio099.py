from time import sleep


def maior(* num):
    cont = maior = 0
    print('=-' * 30)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.4)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


# Programa Principal
maior(3, 5, 2, 6, 8)
maior(5, 7, 3)
maior(9, 7)
maior(6)
maior()
