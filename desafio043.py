peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura * altura)
print('Voce tem o IMC de {:.2f}'.format(imc))
if imc < 18.5:
    print('Voce esta Abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Voce esta no Peso ideal')
elif 25.1 <= imc <= 30:
    print('Voce esta Sobrepeso')
elif 30.1 <= imc <= 40:
    print('Voce esta com Obesidade')
else:
    print('Voce esta comObesidade Morbida')
