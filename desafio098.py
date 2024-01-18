from time import sleep


def contador(ini, fim, p):
    print('=-' * 15)
    print(f'Contagem de {ini} até {fim} de {p}')
    print('=-' * 15)

    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if ini < fim:
        cont = ini
        while cont <= fim:
            print(f'{cont} > ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('Fim!')
    else:
        cont = ini
        while cont >= fim:
            print(f'{cont} > ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora personalize sua contagem!')
i = int(input('Inicio:  '))
f = int(input('Fim:     '))
pas = int(input('Passo: '))
contador(i, f, pas)
