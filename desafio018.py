from math import radians, sin, cos ,tan
num = float(input('Digite o ângulo que você deseja: '))
s = sin(radians(num))
print('O ângulo de {} tem o SENO de {:.2f}'.format(num, s))
c = cos(radians(num))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(num, c))
t = tan(radians(num))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(num, t))
