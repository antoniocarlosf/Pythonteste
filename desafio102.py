def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um numero.
    :param num: O numero a Ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um numero.
    """
    resultado = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(f'{i} x ', end='')
            else:
                print(' = ', end='')
        resultado *= i
    return resultado


# Programa Principal
print('-' * 15)
print(fatorial(5, show=True))
