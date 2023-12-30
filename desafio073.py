colocados = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense',
             'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiaba', 'Corinthians', 'Cruzeiro',
             'Vasco Da Gama', 'Bahia', 'Santos', 'Goias', 'Coritiba', 'América-MG')

print(f'Lista de times do Brasileirão 2023: {colocados}')
print(f'Os 5 primeiros são: {colocados[0: 5]}')
print(f'Os 4 ultimos são: {colocados[-4:]}')
print(f'Times em ordem alfabética: {sorted(colocados)}')
F_posição = colocados.index('Flamengo') + 1
print(f'O Flamengo esta em {F_posição}° posição')
