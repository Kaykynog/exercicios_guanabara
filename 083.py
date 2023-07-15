# Exercício Python 083: Crie um programa onde o usuário 
# digite uma expressão qualquer que use parênteses. Seu 
# aplicativo deverá analisar se a expressão passada está 
# com os parênteses abertos e fechados na ordem correta.

expressao = []
fechando = ')'
abrindo = '('
n = str(input('Digite sua expressão: '))
for s in n:
    if s == abrindo:
        expressao.append(abrindo)
    elif s == fechando:
        if len(expressao) > 0:
            expressao.pop()
        else:
            expressao.append(fechando)
            break
if len(expressao) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')

