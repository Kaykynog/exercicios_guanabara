# Exercício Python 077: Crie um programa que tenha 
# uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra,
# quais são as suas vogais.

frase = (
    'oi', 'eu', 'sou', 'o', 'kayky',
)
for f in frase:
    print(f'\nPara a palavra: {f.upper()} --> ', end='')
    for letra in f:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')