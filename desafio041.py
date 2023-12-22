from datetime import datetime
data_nascimento_str = str(input('Digite sua data de nascimento (formato DD-MM-YYYY): '))
data_nascimento = datetime.strptime(data_nascimento_str, "%d-%m-%Y")
data_atual = datetime.now()
diferenca = data_atual - data_nascimento
idade = diferenca.days // 365
print('Sua idade é de {} anos'.format(idade))
if idade <= 9:
    print('Categoria Mirim')
if 10 <= idade <= 14:
    print('Categoria Infantil')
if 15 <= idade <= 19:
    print('Categoria Junior')
if idade == 20:
    print('Categoria Senior')
if idade >= 21:
    print('Categoria Master')
