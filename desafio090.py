aluno = {}
situação = []
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
situação.append(aluno.copy())
print(f'O nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
if aluno["media"] <= 7:
    print(f'Situação é igual a Reprovado')
else:
    print(f'Situação igual a Aprovado')
