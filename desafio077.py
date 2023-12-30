palavra = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
           'mercado', 'programador', 'futuro')
for palavra_atual in palavra:
    vogais = [letra for letra in palavra_atual if letra.lower() in 'aeiou']
    print(f'A palavra {palavra_atual} tem as vogais {", ".join(vogais)}')
