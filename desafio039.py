from datetime import datetime
data_nascimento_str = str(input('Digite sua data de nascimento (formato DD-MM-YYYY): '))
data_nascimento = datetime.strptime(data_nascimento_str, "%d-%m-%Y")
data_atual = datetime.now()
diferenca = data_atual - data_nascimento
idade = diferenca.days // 365
print('Sua idade é de {} anos'.format(idade))
passou = idade - 18
falta = 18 - idade
if idade == 18:
    print('Esta na hora de se alistar!')
if idade < 18:
    print('Ainda não é hora de se alistar! Faltam {} anos'.format(falta))
if idade > 18:
    print('Ja passou da hora de se alistar! Ja passou {} anos'.format(passou))
