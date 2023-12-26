a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento : '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    if a == b == c:
        print('Triângulo Equilátero')
    elif a == b or a == c or b == c:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
