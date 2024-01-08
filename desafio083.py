expr = str(input('Digite a expressão: '))
monte = []
for simb in expr:
    if simb == '(':
        monte.append('(')
    elif simb == ')':
        if len(monte) > 0:
            monte.pop()
        else:
            monte.append(')')
            break
if len(monte) == 0:
    print('Sua expressão esta valida')
else:
    print('Sua expressão esta invalida')
