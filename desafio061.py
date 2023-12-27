primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (9 + 1) * razao
c = primeiro
while c <= decimo:
    print('{} '.format(c), end=' ')
    c += razao
print('Acabou')
