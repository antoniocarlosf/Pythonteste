from datetime import date


def voto():
    ano = date.today().year
    nascimento = int(input('Em que ano você nasceu? '))
    idade = ano - nascimento
    return idade


idade_voto = voto()
print('--' * 15)
if idade_voto < 18:
    print(f'Com {idade_voto} anos: Não Vota.')
if 18 >= idade_voto or idade_voto < 65:
    print(f'Com {idade_voto} anos: Voto Obrigatório.')
if idade_voto >= 65:
    print(f'Com {idade_voto} anos: Voto Opcional.')
