import random
aleatorio = [random.randint(1, 11) for _ in range(5)]
tupla = aleatorio
print(f'Os valores sorteados foram {tupla}')
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')
