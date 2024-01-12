jogador = {}
jogador['nome'] = str(input('Nome: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []
for g in range(jogador['partidas']):
    gols = int(input(f'Quantos gols na partida {g+1}? '))
    jogador['gols'].append(gols)
tot = sum(jogador["gols"])
jogador['total'] = tot
bio = [jogador.copy()]

print('=-'*20)

print(bio)

print('=-'*20)

print(f'O campo nome tem o valor {jogador["nome"]}.')
print(f'O campo gols tem o valor {jogador["gols"]}.')
print(f'O campo total tem o valor {jogador["total"]}.')

print('=-'*20)

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for p in range(jogador['partidas']):
    print(f'=> Na partida {p+1}, fez {jogador["gols"][p]} gols.')
print(f'Foi um total de {jogador["total"]} gols')
